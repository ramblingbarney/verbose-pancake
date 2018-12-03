from django.conf.urls import url, include
from .views import all_products, new_product, product_area

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^new$', new_product, name='new_product'),
    url(r'^area$', product_area, name='product_area'),
]
