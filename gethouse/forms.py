from django import forms
from .models import *

class AccomodationForm(forms.ModelForm):
    class Meta:
        model = Accomodation
        exclude = ['user']