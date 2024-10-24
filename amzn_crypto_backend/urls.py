"""amzn_crypto_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from amzn_crypto_backend import views as main_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('get-balance-from-wallet-ETH', main_views.get_balance_from_wallet_ETH,
         name='get_balance_from_wallet_ETH'),
    path('lala', main_views.get_balance_from_wallet_USDC, name='index'),
    path('get-price-in-cryptocurrency/<str:from_value>/<str:to_value>/',
         main_views.get_price_in_cryptocurrency,
         name='get_price_in_cryptocurrency'),
    path('transactions/', include('transactions.urls'), name='transactions'),
]
