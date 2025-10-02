from django import forms
from .models import Post, Product, AboutDetail
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class AboutDetailForm(forms.ModelForm):
    class Meta:
        model = AboutDetail
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'is_superuser']
