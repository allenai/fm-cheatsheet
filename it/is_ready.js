/**
 * This script is used by /bin/verify, to determine if the application is
 * ready. The /bin/verify script can't simply hit http://localhost:8080,
 * because on MacOS docker runs in a VM and when the "host" network is used
 * it's the host network of that VM.
 *
 * The script just makes a request to the provided origin. If a 200 response is
 * received it exists with the 0 exit code. If the request fails, or a non-200
 * response is received it exists with a non-zero exit code.
 *
 * The origin should be provided as the first argument to this script, i.e.:
 *
 *      is_ready http://localhost:8080
 *
 */

const http = require('http');

async function checkIfReady(origin) {
    return new Promise((resolve, reject) => {
        const req = http.request(origin, (res) => {
            const isReady = res.statusCode === 200;
            console.log(`${origin} ~> ${res.statusCode}: ${isReady ? 'OK' : 'Not Ready'}`);
            if (isReady) {
                resolve();
            } else {
                reject(new Error(`Response status: ${res.statusCode}`));
            }
        });
        req.on('error', reject);
        req.end();
    });
}

const origin = process.argv[2];
if (!origin) {
    throw Error('You must set an origin. Usage: node is_ready ORIGIN');
}

checkIfReady(origin)
    .then(() => process.exit(0))
    .catch((err) => {
        console.error(`Not ready: ${err}`);
        process.exit(1);
    });
