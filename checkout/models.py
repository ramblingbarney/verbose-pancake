from django.db import models
from products.models import Product
from datetimeutc.fields import DateTimeUTCField


class Sale(models.Model):
    # store the stripe charge id for this sale
    charge_id = models.CharField(max_length=128)
    price_in_cents = models.IntegerField()
    user_id = models.IntegerField()
    submitted = DateTimeUTCField(auto_now_add=True)

    def __str__(self):
        return self.charge_id

class SaleProduct(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product_id
