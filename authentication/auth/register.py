import re

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import MinimumLengthValidator, CommonPasswordValidator
from django.core.exceptions import ValidationError


def validate_mobile_number(value):
    regex = r"^\d{10}$"
    if not re.match(regex, value):
        raise ValidationError("Invalid mobile number format. Please enter 10 digits.")


class Register(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    email = forms.EmailField(label="Email")
    mobile = forms.CharField(label="Mobile Number", validators=[validate_mobile_number])
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput,
                               validators=[
                                   MinimumLengthValidator(8),
                                   CommonPasswordValidator(),
                               ])

