from django.db import models
from sellar.models import Seller


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    parent_category = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='subcategories')

    def __str__(self):
        return self.name


class Product(models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    base_price=models.DecimalField(max_digits=10,decimal_places=2)
    discounted_price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    stock=models.CharField(max_length=50,null=True,blank=True)
    brand=models.CharField(max_length=50,null=True,blank=True)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    seller=models.ForeignKey('sellar.Seller',on_delete=models.CASCADE,related_name='products',null=True,blank=True)

    def __str__(self):
        return self.name
    
class ProductVarient(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='varients')
    color=models.CharField(max_length=50,null=True,blank=True)
    size=models.CharField(max_length=50,null=True,blank=True)
    sku=models.CharField(max_length=100,unique=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    discounted_price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    stock=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return f"{self.product.name}-{self.sku}"
    

class ProductImage(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')
    varient=models.ForeignKey(ProductVarient,on_delete=models.CASCADE,related_name='images',null=True,blank=True)
    image=models.ImageField(upload_to='product_images/')
    is_primary=models.BooleanField(default=False)
    upload_at=models.DateTimeField(auto_now_add=True)




