from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from .views import *
from django.conf import settings
 

urlpatterns = [
    path("", home, name="home"),
    path("techlang/", techlang, name="techlang"),
    path("about/", about, name="about"),
    path("account/", ChangePasswordView.as_view(), name="account"),
    path("account/delete_account", delete_account, name="delete_account"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", authView, name="signup"),
    path("create_project/", createProject, name="create_project"),
    path("details/", displayDetails, name="details")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)