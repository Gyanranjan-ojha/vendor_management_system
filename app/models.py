from django.db import models
import uuid

class Vendor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    contact_details = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'vendor'
        db_table = 'vendors'

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE, db_column="vendor_id")
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(null=True, blank=True)
    items = models.JSONField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20)
    quality_rating = models.FloatField(default=0)
    issue_date = models.DateTimeField(auto_now_add=True)
    acknowledgment_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.po_number

    class Meta:
        verbose_name_plural  = 'purchase_order'
        db_table = 'purchase_orders'

class HistoricalPerformance(models.Model):
    vendor_id = models.ForeignKey(Vendor, on_delete=models.CASCADE, db_column="vendor_id")
    date = models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return f"{self.vendor_id} - {self.date}"

    class Meta:
        verbose_name_plural  = 'historical_performance'
        db_table = 'historical_performances'
