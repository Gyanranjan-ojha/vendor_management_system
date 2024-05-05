"""
URL configuration for app.
"""

from django.urls import path
from .views import *

urlpatterns = [

    path('vendors/', VendorListCreateAPIView.as_view(), name='vendors'),  
    # Get all vendors (GET), Create a vendor (POST)

    path('vendors/<uuid:pk>/', VendorRetrieveUpdateDestroyAPIView.as_view()),  
    # Get, update, delete a vendor (GET, PUT, DELETE)

    path('purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchase_orders'),  
    # Get all purchase orders (GET), Create a purchase order (POST)

    path('purchase_orders/<uuid:pk>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view()),  
    # Get, update, delete a purchase order (GET, PUT, DELETE)
]