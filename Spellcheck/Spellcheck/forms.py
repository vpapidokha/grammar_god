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


        exclude={""}
        extra_field = forms.CharField(label='Name of Institution')
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'Input e-mail','required': True,'type': 'email','autofocus':True}),
            'name': forms.TextInput(attrs={'placeholder': 'Input name', 'required': True}),
            'password': forms.TextInput(attrs={'placeholder': 'Input password','required': True, 'type': 'password'}),

        }

    def clean(self):
        cleaned_data = super(UsersForm, self).clean()
        password = cleaned_data.get("password")
        retypePassword = cleaned_data.get("retypePassword")

        if password != retypePassword:
         raise forms.ValidationError("Passwords does not match!")
