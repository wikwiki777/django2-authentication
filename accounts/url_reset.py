from django.urls import re_path
from django.contrib.auth.views import (PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)


urlpatterns = [
    re_path(r'^$', PasswordResetView.as_view(), name='password_reset'),
    re_path(r'^done$', PasswordResetDoneView.as_view(),
            name='password_reset_done'),
    re_path(r'^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)$',
            PasswordResetConfirmView.as_view(), name='password_reset_confrim'),
    re_path(r'^complete$', PasswordResetCompleteView.as_view(),
            name='password_reset_complete')
]
