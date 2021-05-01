from web3 import Web3, HTTPProvider
import yaml

class OracleProxy:
  def __init__(self, web3_proxy, blockchain, config_dir='config'):
    self.web3_proxy = web3_proxy
    self.blockchain = blockchain
    with open(f'{config_dir}/web3.yaml', 'r') as fp:
      self.config_web3_proxy = yaml.safe_load(fp.read())
    self.web3 = Web3(HTTPProvider(endpoint_uri=self.config_web3_proxy[self.web3_proxy][self.blockchain]))

    with open(f'{config_dir}/contracts.yaml', 'r') as fp:
      self.contracts = yaml.safe_load(fp.read())
    
    with open(f'{config_dir}/abis.yaml', 'r') as fp:
      self.abis = yaml.safe_load(fp.read())

    self.active_contracts = {}

  def get(self, token, provider='chainlink', ref="ETH", round_id=None):
    key = f"{token}/{ref}/{provider}/{self.blockchain}"
    if key not in self.active_contracts.keys():
      self.active_contracts[key] = self.web3.eth.contract(
          address=self.contracts['tokens'][token][ref][provider][self.blockchain], 
          abi=self.abis[provider])
    
    if round_id is None:
      res = self.active_contracts[key].functions.latestRoundData().call()
    else:
      res = self.active_contracts[key].functions.getRoundData(round_id).call()
    
    return {
        'roundId': res[0],
        'answer': res[1],
        'startedAt': res[2],
        'updatedAt': res[3],
        'answeredInRound': res[4]
    }


