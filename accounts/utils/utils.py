import re
from django import forms


def check_whitespace(str):
    return bool(re.search('\s', str))


def validate_username(model, username):
    is_whitespace = check_whitespace(username)
    if is_whitespace:
        raise forms.ValidationError("Username can't contain space")
    try:
        is_username_exists = model.objects.get(username__iexact=username)
        if is_username_exists:
            raise forms.ValidationError("Username already exists")
    except model.DoesNotExist:
        pass
