// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./ERC721.sol";

contract PlayNFT is ERC721 {
    int256 public health;
    address public owner;

    constructor(string memory tokenName, string memory tokenSymbol) ERC721(tokenName, tokenSymbol) {
        owner = msg.sender;
    }

    function getHealth() external view returns (int256){
        return health;
    }

    function updateHealth(int256 new_health) public {
        require(msg.sender == owner, "only owner can update health");
        health = new_health;
    }

}