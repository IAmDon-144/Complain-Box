from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2', "join", "code"]

        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Your Email", }),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Your username"}),

            'join': forms.Select(attrs={'class': 'form-control',}),

            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter Your Code ex.1903000"}),

            

        }
