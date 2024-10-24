# books/urls.py
from django.urls import path
from transactions import views

urlpatterns = [
    path('get-balance-from-wallet-ETH', views.get_balance_from_wallet_ETH,
         name='get_balance_from_wallet_ETH'),
    path('store-purchase-data', views.store_purchase_data, name='store_purchase_data'),
]
