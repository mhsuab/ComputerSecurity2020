const fs = require('fs')
const lib = require('./lib')(require('./config'))

web3 = lib.web3

async function main() {
    let tx = await web3.eth.getTransaction('0x8e1826b2fcaa53bbb9d945ad52b10358fc377ebba3d3a8290555b2e35788c5c1')
    console.log(tx.blockNumber)
    let block = await web3.eth.getBlock(tx.blockNumber)
    console.log(block.timestamp)
}

main()