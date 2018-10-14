from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=20, required=True, help_text = None, widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    email = forms.CharField(max_length=254, required=True, help_text = None, widget=forms.EmailInput(attrs={'placeholder': 'Enter your Email Address'}))
    password1 = forms.CharField(max_length=20, required=True, help_text=None, widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(max_length=20, required=True, help_text=None, widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    image = forms.ImageField(help_text = None, widget = forms.FileInput(attrs = {'style': 'width: 200px; border: 1px solid #d4d9d1; border-radius: 7px;'}))
    full_name = forms.CharField(max_length = 80, help_text = None, widget=forms.TextInput(attrs={'placeholder': 'Enter your Full Name'}))
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$', help_text = None, widget = forms.TextInput(attrs = {'placeholder' : 'Enter your phone number'}))

    class Meta:
        model = Profile
        fields = ('full_name', 'image', 'phone_number')
