from django.contrib import admin
from .models import Seller
# Register your models here.
@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display=('user','store_name','business_type','approval_status','created_at')