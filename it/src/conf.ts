import { URL } from 'url';
import path from 'path';
import fs from 'fs';
import util from 'util';

export namespace conf {
    export class Config {
        constructor(readonly origin: string, readonly fixtureRoot: string) {}

        url() {
            return new URL('', this.origin);
        }

        fixture(file: string) {
            if (path.isAbsolute(file)) {
                throw new Error(`${file} is an absolute path, must be relative`);
            }
            return path.resolve(this.fixtureRoot, file);
        }

        async readFixture(file: string, encoding: string = 'utf-8') {
            // This is gross, but this is the accepted mechanism for producing
            // a version of fs.readFile that can be used with async/await.
            const rd = util.promisify(fs.readFile);
            return rd(this.fixture(file), encoding);
        }

        static fromEnv(): Config {
            // The default, `http://proxy:8080`, is the origin of the NGINX
            // reverse proxy when running things via `docker compose`.
            return new Config(
                process.env.IT_ORIGIN || 'http://proxy:8080',
                process.env.IT_FIXTURE_ROOT || '/it/fixture'
            );
        }
    }
}

export default conf;
