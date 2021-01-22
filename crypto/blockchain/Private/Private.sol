/**
 *Submitted for verification at Etherscan.io on 2020-10-22
*/

/*
    因為每一個節點都會有一個 contract
    所以雖然是 private（只有這個合約可以呼叫）
    但還是可以在節點上直接到 storage 找
*/

// SPDX-License-Identifier: MIT
pragma solidity >=0.7.0;

contract Private {
    string private flag;

    constructor (string memory _flag) {
        flag = _flag;
    }
}