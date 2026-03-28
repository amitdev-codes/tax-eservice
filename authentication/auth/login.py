from django import forms
from django.contrib.auth.password_validation import MinimumLengthValidator, CommonPasswordValidator


class Login(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput,
                               validators=[
                                   MinimumLengthValidator(8),
                                   CommonPasswordValidator(),
                               ])
