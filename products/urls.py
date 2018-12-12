from django.conf.urls import url, include
from .views import all_products, new_product, edit_product, product_area

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^new$', new_product, name='new_product'),
    url(r'^edit/(?P<id>\d+)/$', edit_product, name='edit_product'),
    url(r'^area$', product_area, name='product_area'),
]
