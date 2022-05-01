from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput, CharField
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserForm(ModelForm):

    password = CharField( widget=PasswordInput, label='Пароль')

    class Meta(object):
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
        ]

