from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput, CharField
from django import forms
from .models import Orders, Customers


class UserForm(ModelForm):

    password = CharField(widget=PasswordInput, label='Пароль')

    class Meta(object):
        model = User
        fields = ['username', 'email', 'password']


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
