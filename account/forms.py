from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'customer'    # ← set role
        if commit:
            user.save()
        return user