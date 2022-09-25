// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";

contract PlayNFT is ERC721 {
    uint256 public health;
    address public owner;

    constructor(string memory tokenName, string memory tokenSymbol) ERC721(tokenName, tokenSymbol) {
        owner = msg.sender;
    }

    function updateHealth(uint256 new_health) public {
        require(msg.sender == owner, "only owner can update health");
        health = new_health;
    }

}
