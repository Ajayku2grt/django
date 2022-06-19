from django import forms
from .models import Loginform


class FormloginForm(forms.ModelForm):
    class Meta:
        model= Loginform
        # fields= ["fullname", "email", "contact", "message"] """return all the field from db"""
        fields='__all__'
