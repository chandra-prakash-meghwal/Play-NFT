import os

os.environ['infura_api_key'] = "infura api key"


def get_fast_node_url(network='mainnet'):
    node_url = 'https://{}.infura.io/v3/{}'.format(network, os.environ.get('infura_api_key'))
    print(node_url)
    return node_url