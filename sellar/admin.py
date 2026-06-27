from django.contrib import admin
from .models import Seller


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('user', 'store_name', 'business_type', 'city', 'approval_status', 'created_at')
    list_filter  = ('approval_status', 'business_type')
    search_fields = ('user__username', 'store_name', 'gst_number')
    readonly_fields = ('created_at', 'updated_at')
