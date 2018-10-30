from django.conf.urls import url, include
from django.urls import path
from django.urls import reverse


urlpatterns = [
    url('', include('django.contrib.auth.urls')),
]
