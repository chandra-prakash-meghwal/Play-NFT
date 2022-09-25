// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;


interface IPlayNFT {
    function getHealth() external view returns (int256);
}


contract RefereeContract {
    address public owner;
    uint256 public teamSize;
    address[] private teamA;
    address[] private teamB;

    constructor(uint256 _teamSize) {
        teamSize = _teamSize;
        owner = msg.sender;
    }

    function updateTeamSize(uint256 newTeamSize) public {
        require(msg.sender == owner, "only owner can update health");
        teamSize = newTeamSize;
    }

    function addToTeamA(address nft_address) public {
        require(msg.sender == owner, "only owner can update health");
        require(teamSize >= teamA.length, "team size exceeds");
        teamA.push(nft_address);
    }

    function addToTeamB(address nft_address) public {
        require(msg.sender == owner, "only owner can update health");
        require(teamSize >= teamA.length, "team size exceeds");
        teamB.push(nft_address);
    }


    function getWinner() public view returns (string memory){
        int256 scoreTeamA = 0;
        int256 scoreTeamB = 0;

        for (uint i=0; i<teamA.length; i++) {
            IPlayNFT contractPlayNFT = IPlayNFT(teamA[i]);
            scoreTeamA += contractPlayNFT.getHealth();
        }
        for (uint i=0; i<teamB.length; i++) {
            IPlayNFT contractPlayNFT = IPlayNFT(teamB[i]);
            scoreTeamB += contractPlayNFT.getHealth();
        }
        // IPlayNFT contractPlayNFT = IPlayNFT(0xD4Fc541236927E2EAf8F27606bD7309C1Fc2cbee);
        // contractPlayNFT.getHealth();
        string memory winner;
        if (scoreTeamA > scoreTeamB) {
            winner = "Team A";
        } else {
            winner = "Team B";
        }
        return winner;
    }
}