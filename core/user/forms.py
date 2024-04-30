from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ('email', 'username', 'phone_number')



class UserLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))

