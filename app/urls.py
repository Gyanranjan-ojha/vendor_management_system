"""
URL configuration for app.
"""

from django.urls import path
from .views import *

urlpatterns = [
    #___________________________GET URL paths______________________________
    path('check/', CheckAPIView.as_view(), name='check'),

    #____________________________POST URL paths______________________________
]