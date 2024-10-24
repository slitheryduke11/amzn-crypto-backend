# books/urls.py
from django.urls import path
from transactions import views

urlpatterns = [
    path('get-balance-from-wallet-ETH', views.get_balance_from_wallet_ETH,
         name='get_balance_from_wallet_ETH'),
    path('store-purchase-data', views.store_purchase_data,
         name='store_purchase_data'),
    
    
    
    path('make-purchase', views.make_purchase,
         name='make_purchase'),
    path('is-reward-eligible', views.is_reward_eligible,
         name='is_reward_eligible'),
    path('redeem-reward', views.redeem_reward,
         name='redeem_reward'),
]
