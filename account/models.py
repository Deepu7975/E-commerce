from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    role_choices = [
        ('customer', 'customer'),
        ('seller', 'seller'),
        ('admin', 'admin'),
    ]
    role=models.CharField(max_length=20, choices=role_choices, null=True, blank=True)
    phone_number=models.CharField(unique=True,null=True,blank=True)
    otp=models.IntegerField(null=True,blank=True)
    otp_expiery=models.DateTimeField(null=True,blank=True)
    otp_verified=models.BooleanField(default=False)