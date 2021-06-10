from django import forms
from .models import *

class AccomodationForm(forms.ModelForm):
    class Meta:
        model = Accomodation
        exclude = ['user']


class SubscriptionForm(forms.Form):
    name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')


class ContactForm(forms.Form):
    email = forms.EmailField(label='Email')
    context = forms.CharField(widget=forms.Textarea)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']