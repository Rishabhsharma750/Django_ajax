from django import forms
from .models import Data


class UserForm(forms.Form):
    class Meta:
        model = Data

    fname = forms.CharField(error_messages={'required': 'First name field is required'})
    lname = forms.CharField(error_messages={'required': 'Last name field is required'})
    email = forms.EmailField(error_messages={'required': 'Email field is required'})
    subject = forms.CharField(error_messages={'required': 'Subject field is required'})