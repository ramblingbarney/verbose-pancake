"""issue_tracker_0_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
# from django.urls import path
from django.views import static
from accounts import urls as accounts_urls
from products import urls as products_urls
from home import urls as home_urls
from cart import urls as carts_urls
from checkout import urls as checkout_urls
from comments import urls as comments_urls
from .settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(home_urls)),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^products/', include(products_urls)),
    url(r'^cart/', include(carts_urls)),
    url(r'^checkout/', include(checkout_urls)),
    url(r'^comments/', include(comments_urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
