# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label="Imię",
        required=False,
        max_length=100,
        help_text="Opcjonalnie."
    )

    class Meta:
        model = User
        fields = ("username", "first_name", "password1", "password2", )
