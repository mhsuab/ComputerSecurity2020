const fs = require('fs')
const lib = require('./lib')(require('./config'))

async function main() {
    let factory = lib.contract('0x16cf9e5a5848E40E27751f1c9277291993fE6C4E', JSON.parse(JSON.stringify([
        {
            "anonymous": false,
            "inputs": [
                {
                    "indexed": false,
                    "internalType": "uint256",
                    "name": "token",
                    "type": "uint256"
                }
            ],
            "name": "GetFlag",
            "type": "event"
        },
        {
            "inputs": [],
            "name": "create",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                }
            ],
            "name": "instances",
            "outputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "token",
                    "type": "uint256"
                }
            ],
            "name": "validate",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        }
    ])))
    let instance_address = await factory.view('instances', lib.account.address)
    if (instance_address === '0x0000000000000000000000000000000000000000') {
        await factory.call('create')
        instance_address = await factory.view('instances', lib.account.address)
    }
    console.log(`instance = ${instance_address}`)
    challenge = lib.contract(instance_address, JSON.parse(JSON.stringify([
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_player",
                    "type": "address"
                }
            ],
            "stateMutability": "nonpayable",
            "type": "constructor"
        },
        {
            "inputs": [],
            "name": "callme",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "win",
            "outputs": [
                {
                    "internalType": "bool",
                    "name": "",
                    "type": "bool"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        }
    ])))
    console.log(await challenge.call('callme'));
}

main()