from django.conf.urls import url, include
from accounts.views import logout, login_by_email, registration, user_profile
from accounts import urls_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login_by_email, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'', include(urls_reset))
]
