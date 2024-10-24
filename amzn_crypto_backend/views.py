import json

import requests
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from web3 import Web3


# from amzn_crypto_backend.utils import contract_abi_raw


ETH_API_KEY = '96M61TPJ8HRHBM12FZEMP18ZDVKCPNN7BU'

def store_purchase_info():
    pass

def get_balance_from_wallet_ETH(request):
    web3 = Web3(Web3.HTTPProvider(
        'https://mainnet.infura.io/v3/3f25d19551874d8c99e35a13cd310676'))
    balance_wei = web3.eth.get_balance(
        "0x59d06D5177880A02576d28611fd1bEeA9677A88c")
    balance_eth = f"{web3.from_wei(balance_wei, 'ether'):.18f}"
    return HttpResponse(balance_eth)


def get_balance_from_wallet_USDC(request):
    # 1
    web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/3f25d19551874d8c99e35a13cd310676'))
    
    usdc_contract_abi = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function",
    }
]
    usdc_contract_address = '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eb48'  # USDC en Ethereum

    usdc_contract = web3.eth.contract(address=Web3.to_checksum_address(usdc_contract_address), abi=usdc_contract_abi)

    wallet_address = "0xE7654813d5BC436bAD87D321DCdcCb7eA2a1F566"

    balance = usdc_contract.functions.balanceOf(wallet_address).call()

    print(web3.from_wei(balance, 'ether') * (10 ** 12))




    #print(balance_info)
    return HttpResponse("Hello, world. You're at the amzn_crypto_backend index.")


def query_message(request):
    message = request.GET.get('message', 'No message provided')
    
    # Devolver una respuesta HTTP con el mensaje
    return HttpResponse(f'Message received: {message}')


@api_view(['GET'])
def get_price_in_cryptocurrency(request, from_value, to_value):
    """
    Get the price from a currency to a cryptocurrency
    """
    url = "https://api.etherscan.io/api"

    params = {
        'module': 'stats',
        'action': 'ethprice',
        'apikey': ETH_API_KEY
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 200:
        data = response.json()
        eth_price_usd = data['result']['ethusd']
        data = {
            "response": eth_price_usd,
        }
    else:
        data = {"response": "Error"}

    return Response(data)
