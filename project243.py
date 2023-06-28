from web3 import Web3
from web3.middleware import geth_poa_middleware


API_url = 'https://mainnet.infura.io/v3/0e57d739b12943e9b5fc42438625c61b'
web3 = Web3(Web3.HTTPProvider(API_url))
Block_data = web3.eth.get_block(17581162)
count=web3.eth.get_block_transaction_count(17581162)
print("get_block_transaction_count=",count)
fee=web3.eth.fee_history(104,"latest",None)
print("fee=",fee)