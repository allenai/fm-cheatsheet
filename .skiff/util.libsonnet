/**
 * This file contains a few helper methods that are used in webapp.jsonnet.
 * They're put here as to not distract the reader from the stuff that really matters --
 * that is the code that produces their application's configuration.
 */
{
    local util = self,

    /**
     * We're pinned to jsonnet 0.12.0, std.any was added after that version.
     * So we implement our own.
     */
    any(list):
        std.length(std.filter(function(x) x, list)) > 0,

    isCustomHost(host):
        if std.endsWith(host, '.allen.ai') then
            if std.length(std.split(host, '.')) != 3 then
                true
            else
                false
        else if std.endsWith(host, '.apps.allenai.org') then
            if std.length(std.split(host, '.')) != 4 then
                true
            else
                false
        else
            true,

    /**
     * Groups by the provided TLDs. Returns a tuple. The first value is a map of hosts
     * by TLD. The second a list of hosts that didn't match a TLD.
     */
    groupHosts(hosts, tlds):
        local byTLD = { [tld]: std.filter(function(host) std.endsWith(host, tld), hosts) for tld in tlds };
        local rest = std.filter(function(host) !self.any([ std.endsWith(host, tld) for tld in tlds ]), hosts);
        [ byTLD, rest ],

    hasCustomHost(hosts):
        std.length(std.filter(util.isCustomHost, hosts)) > 0,

    /**
     * Returns a list of hostnames, given the provided environment identifier, Skiff config
     * and top level domain.
     */
    getHosts(env, config, tld):
        if env == 'prod' then
            [ config.appName + tld ]
        else
            [ config.appName + '-' + env + tld ],

    /**
     * Returns a few TLS related constructs given the provided hosts. If the application is
     * only using direct subdomains of `.apps.allenai.org` then an empty configuration is provided,
     * as the wildcard certificate that's managed by Skiff Bermuda can be used instead.
     */
    getTLSConfig(fqn, hosts): {
        local needsTLSCert = util.hasCustomHost(hosts),

        ingressAnnotations:
            if needsTLSCert then
                { 'cert-manager.io/cluster-issuer': 'letsencrypt-prod' }
            else {},
        spec:
            if needsTLSCert then
                { secretName: fqn + '-tls' }
            else
                {},
    },

    /**
     * Returns the path to authenticate requets with our Skiff Login system (OAuth2 Proxy).
     * If config has an array of strings in the field "login_allowed_emails", then they are
     * used to limit access to account with those email addresses.
     */
    authPath(config):
      if !('login_allowed_emails' in config) then
          '/oauth2/auth'
      else if std.length(config.login_allowed_emails) > 0 then
          '/oauth2/auth?allowed_emails=' + std.join(',', config.login_allowed_emails),

    /**
     * Returns Ingress annotations that enable authentication, given the provided Skiff config.
     */
    getAuthAnnotations(config, tld):
        if !('login' in config) then
            {}
        else if config.login == "ai2" then
            {
                'nginx.ingress.kubernetes.io/auth-url': 'https://ai2.login' + tld + $.authPath(config),
                'nginx.ingress.kubernetes.io/auth-signin': 'https://ai2.login' + tld + '/oauth2/start?rd=https://$host$request_uri',
                'nginx.ingress.kubernetes.io/auth-response-headers': 'X-Auth-Request-User, X-Auth-Request-Email'
            }
        else if config.login == "google" then
            {
                'nginx.ingress.kubernetes.io/auth-url': 'https://google.login' + tld + $.authPath(config),
                'nginx.ingress.kubernetes.io/auth-signin': 'https://google.login' + tld + '/oauth2/start?rd=https://$host$request_uri',
                'nginx.ingress.kubernetes.io/auth-response-headers': 'X-Auth-Request-User, X-Auth-Request-Email'
            }
        else
            error 'Unknown login type: ' + config.login,
}

