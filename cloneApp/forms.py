from django.core import validators
from django import forms
from .models import User


class Registration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','number','message']
        labels = {'name':'Fill Name','email':'Your Email','number':'Ph Number','message':'Your Message'}
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'number':forms.NumberInput(attrs={'class':'form-control'}),
            'message':forms.TextInput(attrs={'class':'form-control'}),
        }