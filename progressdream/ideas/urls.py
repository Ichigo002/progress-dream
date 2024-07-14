from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("account/", ChangePasswordView.as_view(), name="account"),
    path("account/delete_account", delete_account, name="delete_account"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", authView, name="signup"),
]