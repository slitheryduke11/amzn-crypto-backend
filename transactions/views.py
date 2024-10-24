from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from web3 import Web3
from transactions import utils
from transactions.models import CryptoCurrency, Purchase


@api_view(['GET'])
def store_purchase_data(request):
    # Checks
    if (not request.GET.get("usd_price") or
            not request.GET.get("purchase_id") or
            not request.GET.get("crypto_currency_id") or
            not request.GET.get("crypto_value") or
            not request.GET.get("purchase_date")):
        return Response(status=400)
    try:
        purchase_date = datetime.strptime(
            request.GET.get("purchase_date"), '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return Response(status=400)
    crypto_currency_object = CryptoCurrency.objects.filter(
        symbol=request.GET.get("crypto_currency_id")).first()
    if not crypto_currency_object:
        return Response(
            {"error": "Crypto currency not found"},
            status=400)

    # Store purchase data
    purchase = Purchase(
        usd_price=float(request.GET.get("usd_price")),
        purchase_id=request.GET.get("purchase_id"),
        crypto_currency_id=crypto_currency_object.id,
        crypto_value=float(request.GET.get("crypto_value")),
        purchase_date=purchase_date
    )
    purchase.save()
    # Return response with status 200
    return Response(status=200)



@api_view(['GET'])
def get_balance_from_wallet_ETH(request):
    web3 = Web3(Web3.HTTPProvider(utils.MAINET_INFURA_URL + utils.INFURA_KEY))
    balance_wei = web3.eth.get_balance(utils.AMAZON_WALLET_ADDRESS_ETH)
    balance_eth = f"{web3.from_wei(balance_wei, 'ether'):.18f}"
    data = {
        "response": balance_eth,
    }
    return Response(data)
