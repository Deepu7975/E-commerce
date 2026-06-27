from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
# admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category','base_price','discounted_price',
                  'is_active','created_at','updated_at','description','stock','brand')
admin.site.register(Product,ProductAdmin)

class ProductVarientAdmin(admin.ModelAdmin):
    list_display=('product','sku','color','size','price','discounted_price','stock')
admin.site.register(ProductVarient,ProductVarientAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display=('product','image','varient','is_primary','upload_at')
admin.site.register(ProductImage,ProductImageAdmin)


