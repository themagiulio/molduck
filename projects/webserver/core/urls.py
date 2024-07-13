from django.contrib import admin
from django.urls import path
from molduck.api import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", api.urls, name="1.0.0"),
]
