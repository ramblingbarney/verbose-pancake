from django.contrib import admin
from .models import Product, ProductArea, ProductVote

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductArea)
admin.site.register(ProductVote)
