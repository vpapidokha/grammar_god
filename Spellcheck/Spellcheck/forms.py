from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User

class UsersForm(ModelForm):
    retypePassword = forms.CharField(max_length=50, widget=forms.TextInput(
            attrs={'placeholder': 'Retype password', 'required': True, 'type': 'password'}),
    )

    class Meta:
        model=User

        fields=["username", "email", "password"]

        #extra_field = forms.CharField(label='Name of Institution')
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Input e-mail','required': True,'type': 'email','autofocus':True}),
            'username': forms.TextInput(attrs={'placeholder': 'Input login', 'required': True}),
            #'first_name': forms.TextInput(attrs={'placeholder': 'First name', 'required': True, 'type': 'text'}),
            #'last_name': forms.TextInput(attrs={'placeholder': 'Last name', 'required': True, 'type': 'text'}),
            'password': forms.TextInput(attrs={'placeholder': 'Input password','required': True, 'type': 'password'}),
           # 'retypePassword': forms.TextInput(attrs={'placeholder': 'Retype password', 'required': True, 'type': 'password'}),
        }
        help_texts = {
            'username' : '',
        }

    def clean(self):
        cleaned_data = super(UsersForm, self).clean()
        password = cleaned_data.get("password")
        retypePassword = cleaned_data.get("retypePassword")

        if password != retypePassword:
         raise forms.ValidationError("Passwords does not match!")
