from solcx import compile_standard, install_solc
from web3 import Web3
from .node_urls import get_fast_node_url
from .deployed_contract import deployed_nfts
import json  # to save the output in a JSON file

with open("./contracts/RefereeContract.sol", "r") as file:
    referee_contract_file = file.read()

install_solc("0.8.0")

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"RefereeContract.sol": {"content": referee_contract_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"]
                    # output needed to interact with and deploy contract
                }
            }
        },
    },
    base_path='/home/chandra/Desktop/ardnahc/Play-NFT/contracts',  # change it as per your working directory
    allow_paths='*',
    solc_version="0.8.0",
)

print(compiled_sol)

with open("referee_compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)

bytecode = compiled_sol["contracts"]["RefereeContract.sol"]["RefereeContract"]["evm"]["bytecode"]["object"]

abi = json.loads(compiled_sol["contracts"]["RefereeContract.sol"]["RefereeContract"]["metadata"])["output"]["abi"]


def deploy_referee_contract(owner_address, owner_private_key, team_size, network):
    w3 = Web3(Web3.HTTPProvider(get_fast_node_url(network=network)))
    # address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
    # private_key = (
    #     "0x4f3edf983ac636a65a842ce7c78d9aa706d3b113bce9c46f30d7d21715b23b1d"
    # )
    address = owner_address
    private_key = (
        owner_private_key
    )

    referee_contract = w3.eth.contract(abi=abi, bytecode=bytecode)

    nonce = w3.eth.getTransactionCount(address)

    transaction = referee_contract.constructor(team_size).buildTransaction(
        {"chainId": w3.eth.chain_id, "gasPrice": w3.eth.gas_price, "from": address, "nonce": nonce}
    )

    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)

    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)

    print("Waiting for transaction to finish...")
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    print("Done! Contract deployed to {}".format(transaction_receipt.contractAddress))


def main(owner_address, owner_private_key, network='ropsten', team_size=5):
    deploy_referee_contract(
        owner_address=owner_address,
        owner_private_key=owner_private_key,
        team_size=team_size,
        network=network
    )


def add_to_team(referee_contract_address, nft_address, team_name, owner_address, owner_private_key, network):
    w3 = Web3(Web3.HTTPProvider(get_fast_node_url(network=network)))
    address = owner_address
    private_key = (
        owner_private_key
    )

    play_nft = w3.eth.contract(address=referee_contract_address, abi=abi)

    nonce = w3.eth.getTransactionCount(address)

    if team_name == 'A':
        transaction = play_nft.functions.addToTeamA(nft_address).buildTransaction(
            {"chainId": w3.eth.chain_id, "gasPrice": w3.eth.gas_price, "from": address, "nonce": nonce}
        )
    else:
        transaction = play_nft.functions.addToTeamB(nft_address).buildTransaction(
            {"chainId": w3.eth.chain_id, "gasPrice": w3.eth.gas_price, "from": address, "nonce": nonce}
        )
    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)

    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)

    print("Waiting for transaction to finish...")
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)

    print("Health Updated! ", transaction_receipt)


def create_teams(owner_address, owner_private_key, referee_contract_address, network='ropsten'):
    team_a = ['CSCO', 'TCS', 'RELIANCE', 'SOC', 'CWP']
    team_b = ['BBS', 'BBP', 'ZMT', 'JZH', 'TM']
    for nft in deployed_nfts:
        nft_address = nft['contract_address']
        if nft['stock_symbol'] in team_a:
            team_name = 'A'
            add_to_team(referee_contract_address, nft_address, team_name, owner_address, owner_private_key, network)
        elif nft['stock_symbol'] in team_b:
            team_name = 'B'
            add_to_team(referee_contract_address, nft_address, team_name, owner_address, owner_private_key, network)


def get_winner(referee_contract_address, network='ropsten'):
    w3 = Web3(Web3.HTTPProvider(get_fast_node_url(network=network)))
    play_nft = w3.eth.contract(address=referee_contract_address, abi=abi)
    token_health = play_nft.functions.getWinner().call()
    return token_health

