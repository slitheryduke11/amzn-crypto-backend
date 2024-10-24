from django.contrib import admin

from .models import CryptoCurrency, Purchase


admin.site.register(CryptoCurrency)
admin.site.register(Purchase)
