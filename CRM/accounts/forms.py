from django.forms import ModelForm
from .models import Order, Product, Client
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'surname', 'phone', 'email']

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'name_model', 'engine_fuel', 'car_color']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'product', 'status']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]