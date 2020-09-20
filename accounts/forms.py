from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User
from .utils import utils


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "username",)

    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data.get('username', '')
        utils.validate_username(User, username)
        return username


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "gender",)
