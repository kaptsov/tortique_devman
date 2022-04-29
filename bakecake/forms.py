from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import Orders, Customers


class MyForm(UserCreationForm):

    email = forms.EmailField(max_length=200, help_text='Required')
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class OrderForm(ModelForm):

    class Meta:
        model = Orders
        fields = [
            'level',
            'form',
            'topping',
            'berries',
            'decor',
            'title',
            'comment'
        ]


class CustomerForm(ModelForm):
    class Meta:
        model = Customers
        fields = [
            'first_name',
            'phone_number',
            'address'
        ]
