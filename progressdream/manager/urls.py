from django.urls import path, include
from .views import *

urlpatterns = [
    path("", hub, name="hub"),
    path("create/new_project", new_project, name="new_project"),
    path("create/new_language", new_language, name="new_language"),
    path("create/new_tech", new_tech, name="new_tech"),
    #add more...
]
