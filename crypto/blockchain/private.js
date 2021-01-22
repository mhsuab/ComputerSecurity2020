const fs = require('fs')
const lib = require('./lib')(require('./config'))

async function main() {
    let challenge = lib.contract('0x21546f53ac81ddfc2b618d5617d173e43661366c', JSON.parse(JSON.stringify([
        {
            "inputs": [
                {
                    "internalType": "string",
                    "name": "_flag",
                    "type": "string"
                }
            ],
            "stateMutability": "nonpayable",
            "type": "constructor"
        }
    ])))
    console.log(await challenge.storage(0));
    console.log(await challenge.storage(1));
}

main()