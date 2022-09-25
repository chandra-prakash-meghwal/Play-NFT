from solcx import compile_standard, install_solc
from web3 import Web3
from .node_urls import get_fast_node_url
from .nfts_list import all_nfts
import json  # to save the output in a JSON file


with open("./contracts/PlayNFT.sol", "r") as file:
    play_nft_file = file.read()

install_solc("0.8.0")

compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {"PlayNFT.sol": {"content": play_nft_file}},
        "settings": {
            "outputSelection": {
                "*": {
                    "*": ["abi", "metadata", "evm.bytecode", "evm.bytecode.sourceMap"] # output needed to interact with and deploy contract 
                }
            }
        },
    },
    base_path='/home/chandra/Desktop/ardnahc/Play-NFT/contracts',
    allow_paths='*',
    solc_version="0.8.0",
)

print(compiled_sol)

with open("compiled_code.json", "w") as file:
    json.dump(compiled_sol, file)


bytecode = compiled_sol["contracts"]["PlayNFT.sol"]["PlayNFT"]["evm"]["bytecode"]["object"]

abi = json.loads(compiled_sol["contracts"]["PlayNFT.sol"]["PlayNFT"]["metadata"])["output"]["abi"]


def deploy_nft_contract(owner_address, owner_private_key, token_name, token_symbol, network):
    w3 = Web3(Web3.HTTPProvider(get_fast_node_url(network=network)))
    # address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
    # private_key = (
    #     "0x4f3edf983ac636a65a842ce7c78d9aa706d3b113bce9c46f30d7d21715b23b1d"
    # ) 
    address = owner_address
    private_key = (
        owner_private_key
    ) 

    play_nft = w3.eth.contract(abi=abi, bytecode=bytecode)
    
    nonce = w3.eth.getTransactionCount(address)
    
    transaction = play_nft.constructor(token_name, token_symbol).buildTransaction(
        {"chainId": w3.eth.chain_id, "gasPrice": w3.eth.gas_price, "from": address, "nonce": nonce}
    )
    
    sign_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    
    transaction_hash = w3.eth.send_raw_transaction(sign_transaction.rawTransaction)
    
    print("Waiting for transaction to finish...")
    transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
    print("Done! Contract deployed to {}".format(transaction_receipt.contractAddress))


def main(owner_address, owner_private_key, network='ropsten'):
    for nft in all_nfts:
        print(nft)
        deploy_nft_contract(
            owner_address=owner_address, 
            owner_private_key=owner_private_key, 
            token_name=nft['name'], 
            token_symbol=nft['symbol'], 
            network=network
        )
    # deploy_nft_contract(
    #     owner_address=owner_address, 
    #     owner_private_key=owner_private_key, 
    #     token_name='CHAN', 
    #     token_symbol='CHA', 
    #     network=network
    # )  # ropsten deployed contract address 0xC292f9Fa23Fb956761B6102bb39eD95e4d891047
        