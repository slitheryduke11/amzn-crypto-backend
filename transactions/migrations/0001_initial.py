# Generated by Django 5.1.2 on 2024-10-24 21:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoCurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd_price', models.FloatField()),
                ('purchase_id', models.CharField(max_length=100)),
                ('crypto_value', models.FloatField()),
                ('purchase_date', models.DateField()),
                ('crypto_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.cryptocurrency')),
            ],
        ),
    ]
