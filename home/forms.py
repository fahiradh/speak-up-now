from django import forms
from django.contrib.auth.forms import UserCreationForm
from home.models import Pengguna

class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )    
    is_konsulir = forms.BooleanField(
        widget = forms.CheckboxInput(),
        required = False
    )

    class Meta:
        model = Pengguna
        fields = ('username', 'password1', 'password2', 'is_konsulir')
        

