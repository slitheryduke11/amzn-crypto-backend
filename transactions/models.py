from django.db import models

class CryptoCurrency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    usd_price = models.FloatField()
    purchase_id = models.CharField(max_length=100, unique=True)
    crypto_currency = models.ForeignKey(
        CryptoCurrency, on_delete=models.CASCADE
    )
    crypto_value = models.FloatField()
    purchase_date = models.DateTimeField()

    def __str__(self):
        return self.purchase_id
