from django.conf.urls import re_path, include
from accounts.views import logout, login, registration, user_profile
from accounts import url_reset


urlpatterns = [
    re_path(r'^logout$', logout, name='logout'),
    re_path(r'^login$', login, name='login'),
    re_path(r'^register$', registration, name='register'),
    re_path(r'^profile$', user_profile, name='profile'),
    re_path(r'^password-reset/', include(url_reset)),
]
