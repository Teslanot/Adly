from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from add.models import Advertisement
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 

class AdvertisementForm(forms.Form):
    title       = forms.CharField(max_length=100, widget=forms.TextInput(
        {"class": "form-control-lg"}
    ))
    descriptions = forms.CharField(widget=forms.Textarea(
        {"class": "form-control-lg"}
    ))
    prices       = forms.DecimalField(widget=forms.NumberInput(
        {"class": "form-control-lg"}
    ))
    auction     = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        {"class": "form-check-input"}
    ))
    image       = forms.ImageField(required= False, widget=forms.FileInput(
        {"class": "form-control-lg"}
    ))

    title.widget.attrs.update({'class': 'special'})



    def clean_recipients(self):
        datab = self.cleaned_data['title']
        if "?" not in datab:
            raise ValidationError("?")

        return datab





