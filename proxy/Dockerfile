FROM nginx:1.17.0-alpine

COPY nginx.conf /etc/nginx/nginx.conf

ARG CONF_FILE=local.conf
COPY $CONF_FILE /etc/nginx/conf.d/default.conf

COPY proxy.conf /etc/nginx/includes/proxy.conf

# robots.txt
COPY robots.txt ./robots.txt
RUN mkdir /robots
COPY robots.txt /robots