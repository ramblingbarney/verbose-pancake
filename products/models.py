from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    # this the minimum amout required to fix the issue
    min_payment = models.DecimalField(max_digits=6, decimal_places=2)
    # this is the cumulative amount paid by users to fix the issue
    total_amount_paid = models.DecimalField(max_digits=6, decimal_places=2)
    # product area is networking, front ui, backend, db report
    product_area = models.CharField(max_length=254, default='')
    # product_need is urgency low, medium or high
    product_need = models.CharField(max_length=254, default='')
    # product_complexity is urgency low, medium or high
    product_complexity = models.CharField(max_length=254, default='')
    # image of product and/or proposed functional enhancement
    image = models.ImageField(upload_to='images')
    # technical documenation related to the product
    # and/or proposed functional enhancement
    product_documents = models.ImageField(upload_to='product_documents')

    def __str__(self):
        return self.name
