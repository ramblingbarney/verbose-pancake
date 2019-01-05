from django.conf.urls import url
from checkout import views


urlpatterns = [
    url(r'^charge/(?P<total_sale_price>\d+\.\d{2})/$', views.charge, name="charge"),
]
