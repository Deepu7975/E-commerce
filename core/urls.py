from django.urls import path
from . import views

urlpatterns=[
    path('add_product/',views.add_product,name='add_product'),
    path('product_varient/<int:product_id>/',views.product_varient,name='add_varient'),
    path('product_image/',views.product_image,name='product_image'),
    path('display_products/',views.display_products,name='display_products'),
    path('display_varients/<int:product_id>/',views.display_varients,name='varients'),
    path('add_image/<int:varient_id>',views.add_image,name='add_image'),
    path('home/',views.product_list,name='home'),
]