from rest_framework import serializers
from .models import Vendor, PurchaseOrder

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name', 'contact_details', 'address', 'vendor_code']
    
    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance


class PurchaseOrderSerializer(serializers.ModelSerializer):

    vendor_name = serializers.CharField(source='vendor_id.name', read_only=True)

    class Meta:
        model = PurchaseOrder
        fields = ['id', 'po_number', 'vendor_id', 'vendor_name', 'order_date', 'delivery_date', 'items', 'quantity', 'status']

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance
