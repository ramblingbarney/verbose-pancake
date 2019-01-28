from django.conf.urls import url, include
from .views import view_comments, edit_comments

urlpatterns = [
    url(r'^edit/(?P<id>\d+)/(?P<name>[\w\d\s]+)/$',
        edit_comments, name="edit_comments"),
    url(r'^view/(?P<id>\d+)/(?P<name>[\w\d\s]+)/$',
        view_comments, name="view_comments"),
]
