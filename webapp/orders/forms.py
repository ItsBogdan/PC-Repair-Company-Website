from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Order, ListOfServices
from django import forms
from django.contrib.auth.models import User

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['device', 'service']
        labels = {
            'service': 'Услуга',
            'device': 'Устройство'
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30, label='Имя пользователя')
    password = forms.CharField(widget=forms.PasswordInput, max_length=30, label='Пароль')

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль', strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    password2 = forms.CharField(label='Подтвердите пароль', strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    phone_number = forms.CharField(max_length=12)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'username', 'password1']
        labels = {
            'username': 'Имя пользователя',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'phone_number': 'Номер телефона',
            'email': 'Адрес эл.почты',
            'password2': 'Пароль'
        }
        help_texts = {
            'username': None,
            'password': None
        }