from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserAuthenticationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        username = self.data.get('username')
        password = self.data.get('password')