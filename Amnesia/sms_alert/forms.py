from django import forms
from .models import User
from timezone_field import TimeZoneFormField


class UserForm(forms.Form):
    timezone = TimeZoneFormField()

