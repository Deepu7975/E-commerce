from django.urls import path
from . import views

urlpatterns = [
    path('sellar_register/', views.sellar_register_view, name='sellar_register'),
    path('sellar_signin/',   views.sellar_signin_view,   name='sellar_signin'),
    path('logout/',          views.sellar_logout_view,   name='sellar_logout'),   # ✅ added
    path('profile/',         views.seller_profile_view,  name='seller_profile'),  # ✅ added
]
