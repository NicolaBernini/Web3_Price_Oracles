from src.oracle_proxy import OracleProxy

cl = OracleProxy(web3_proxy='infura', blockchain='mainnet')

temp = cl.get(token='1INCH', ref='ETH')

print(f"Getting 1INCH/ETH from Chainlink on Ethereum Mainnet\n{temp}")
