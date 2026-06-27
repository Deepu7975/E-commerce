from django.db import models
from account.models import User
# Create your models here.

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='seller_profile')
    store_name = models.CharField(max_length=150, null=True, blank=True)
    store_description = models.TextField(null=True, blank=True)
    business_type = models.CharField(max_length=50, choices=[
        ('Individual', 'Individual'),
        ('Company', 'Company')
    ], null=True, blank=True)
    gst_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    email_verified = models.BooleanField(default=False)
    approval_status = models.CharField(max_length=20, choices=[
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('rejected', 'rejected')
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username