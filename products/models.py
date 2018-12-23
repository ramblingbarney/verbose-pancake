import os
from django.db import models
from django.forms import ModelForm
from django.db.models import Count
from django.core.validators import FileExtensionValidator
from datetimeutc.fields import DateTimeUTCField


class ProductArea(models.Model):
    name = models.CharField(max_length=254, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    THREE_CHOICES = (
        ('L', 'Low'),
        ('M', 'Medium'),
        ('H', 'High'),
    )

    STATUS = (
        ('T', 'To Do'),
        ('D', 'Doing'),
        ('C', 'Complete'),
    )

    PRODUCT_TYPE = (
        ('I', 'Issue'),
        ('F', 'Feature'),
    )

    name = models.CharField(max_length=254, blank=False)
    description = models.TextField(blank=False)
    # this is the amount to be paid for the feature/issue
    # to be added to the total_amount_paid
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # this is the cumulative amount paid by users to fix the issue
    total_amount_paid = models.DecimalField(
        max_digits=6, decimal_places=2, default=0.00)
    # product area
    product_area = models.ForeignKey(ProductArea, on_delete=models.CASCADE)
    # product_need is urgency
    product_need = models.CharField(max_length=1, choices=THREE_CHOICES)
    # product_complexity is urgency
    product_complexity = models.CharField(max_length=1, choices=THREE_CHOICES)
    # status of the freature or issue
    status = models.CharField(max_length=1, choices=STATUS)
    # product type bug/issue or feature
    product_type = models.CharField(max_length=1, choices=PRODUCT_TYPE)
    # image of product and/or proposed functional enhancement
    image = models.ImageField(upload_to='images', blank=True)
    # technical documenation related to the product
    # and/or proposed functional enhancement
    product_document = models.FileField(
        upload_to='product_documents',
        blank=True,
        validators=[FileExtensionValidator(
            allowed_extensions=['pdf', 'doc', 'docx', 'txt'])])

    @property
    def filename(self):
        return os.path.basename(self.product_document.name)

    @property
    def total_votes(self):
        return self.productvote_set.count()

    def save(self, *args, **kwargs):
        # object already exists in db
        if self.pk:
            old_model = Product.objects.get(pk=self.pk)

            if self.image is None:
                self.image = old_model.image

            if self.product_document is None:
                self.product_document = old_model.product_document

        # call the inherited save method
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ProductVote(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    submitted = DateTimeUTCField(auto_now_add=True)

    def __str__(self):
        return self.product
