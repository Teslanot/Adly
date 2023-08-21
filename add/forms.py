from django import forms
from django.core.validators import RegexValidator


class AdverisementForm(forms.Form):
    # class="row mb-3 offset-sm-4"
    title       = forms.CharField(max_length=100, widget=forms.TextInput(
        {"class": "form-control-lg"}
    ), validators=[RegexValidator('[?+-/%]', inverse_match=True)]) # validators работает
    descriptions = forms.CharField(widget=forms.Textarea(
        {"class": "form-control-lg"}
    ))
    prices       = forms.DecimalField(widget=forms.NumberInput(
        {"class": "form-control-lg"}
    ))
    auction     = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        {"class": "form-check-input"}
    )) # поле необязательное
    image       = forms.ImageField(widget=forms.FileInput(
        {"class": "form-control-lg"}
    ))

    # title.widget.attrs.update({'class': 'special'})


    # def clean_recipients(self):
    #     data = self.cleaned_data['title']
    #     if "?" not in data:
    #         raise ValidationError("?")

    #     # Always return a value to use as the new cleaned data, even if
    #     # this method didn't change it.
    #     return data






