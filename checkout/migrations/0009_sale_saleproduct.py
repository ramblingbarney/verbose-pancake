# Generated by Django 2.1.1 on 2019-01-15 22:13

import datetimeutc.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0008_product_productvote'),
        ('checkout', '0008_auto_20190115_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_id', models.CharField(max_length=128)),
                ('price_in_cents', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('submitted', datetimeutc.fields.DateTimeUTCField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SaleProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.Sale')),
            ],
        ),
    ]
