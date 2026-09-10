import os
from web3 import Web3
BASE_RPC=os.getenv("BASE_RPC_URL","https://mainnet.base.org")
w3=Web3(Web3.HTTPProvider(BASE_RPC))
def mint_rwa_nft(to_address, metadata):
    print(f"[Base 8453] Mint to {to_address} {metadata}")
    return "0x"+"a"*16+"b"*16+"c"*32+" - DEMO TX - add BASE_RPC_URL for real"
def get_chain_info():
    try:
        return {"chain_id":w3.eth.chain_id,"block":w3.eth.block_number}
    except:
        return {"chain_id":8453,"block":"offline demo"}