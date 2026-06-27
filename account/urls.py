from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerview, name='register'),
    path('signin/',   views.signinview,   name='signin'),
    path('logout/',   views.logoutview,   name='logout'),   # ✅ added
]
