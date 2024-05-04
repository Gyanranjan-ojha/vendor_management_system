"""
URL configuration for core project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework.routers import DefaultRouter

admin.site.site_header = settings.ADMIN_SITE_HEADER

router = DefaultRouter()

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('',include(router.urls)),
    path('api/',include('app.urls')),
]
