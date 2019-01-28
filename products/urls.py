from django.conf.urls import url
from .views import all_products, new_product, edit_product, delete_product
from .views import all_product_areas, new_product_area
from .views import edit_product_area, delete_product_area

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^new$', new_product, name='new_product'),
    url(r'^edit/(?P<id>\d+)/$', edit_product, name='edit_product'),
    url(r'^(?P<id>\d+)/delete$', delete_product, name='delete_product'),
    url(r'^areas$', all_product_areas, name='product_areas'),
    url(r'^area/new$', new_product_area, name='new_product_area'),
    url(r'^area/edit/(?P<id>\d+)/$',
        edit_product_area, name='edit_product_area'),
    url(r'^area/(?P<id>\d+)/delete$',
        delete_product_area, name='delete_product_area'),
]
# TODO: avoid page not found errors, redirect to home
