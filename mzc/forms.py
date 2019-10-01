from django import forms

from .models import faculity

class faculityform(forms.Modelform):
     
     class Meta:
         model=faculity
         fields='__all__'