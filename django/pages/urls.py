

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
]
# pages/urls.py
from django.urls import path
from .views import home_page_view

urlpatterns = [
    path("", home_page_view),
]