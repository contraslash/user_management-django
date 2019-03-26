from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation
from django.utils.translation import ugettext_lazy as _


class UserGroups(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'groups',
        )
        widgets = {
            'groups': forms.SelectMultiple(attrs={"class": "form-control select2"})
        }


class CustomUserForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta(UserCreationForm.Meta):
        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
        }