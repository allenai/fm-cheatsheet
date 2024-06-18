import axios from 'axios';

import assert from 'assert';

import conf from './conf';

/**
 * Returns the mime-type and optional charset expressed in the provided string,
 * which is presumedly the value of the HTTP Content-Type header. The values
 * are converted to lowercase before being returned.
 *
 * We do this so that the tests pass in both the development environment and
 * when running with production settings. The charset is returned as UTF-8 by
 * the server used to serve the UI in development, and utf-8 by NGINX when
 * using production settings.
 */
function parseContentType(header: string): { mimeType: string; charset?: string } {
    const [mimeType, rawCharset] = header.toLowerCase().split(';');
    const charset = (rawCharset ?? '').split('=')[1];
    return { mimeType, charset };
}

describe('/', () => {
    it('returns a 200', async () => {
        const config = conf.Config.fromEnv();

        const url = config.url();
        url.pathname = '/';

        const resp = await axios.get(url.toString());

        assert.strictEqual(resp.status, 200);
        assert.deepStrictEqual(parseContentType(resp.headers['content-type']), {
            mimeType: 'text/html',
            charset: 'utf-8',
        });
    });
});


describe('/robots.txt', () => {
    it('returns the expected response', async () => {
        const config = conf.Config.fromEnv();

        const url = config.url();
        url.pathname = '/robots.txt';

        const resp = await axios.get(url.toString());

        assert.strictEqual(resp.status, 200);
        assert.deepStrictEqual(parseContentType(resp.headers['content-type']), {
            mimeType: 'text/plain',
            charset: 'utf-8',
        });

        const robotsTxt = await config.readFixture('robots.txt');
        assert.strictEqual(resp.data, robotsTxt);
    });
});
