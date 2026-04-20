from django.db import models
from django.contrib.auth.models import User # Required for the 'handled_by' field
from products.models import Product

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('IN', 'Stock In (Received)'),
        ('OUT', 'Stock Out (Issued)'),
    )
    
    # Requirement: Transactions app must include status fields
    STATUS_CHOICES = (
        ('COMPLETED', 'Completed'),
        ('PENDING', 'Pending'),
        ('CANCELLED', 'Cancelled'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPES)
    quantity = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True) # Requirement: Date/Time field
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='COMPLETED')
    handled_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) # Tracks the staff/admin
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.product.name} ({self.quantity}) - {self.status}"