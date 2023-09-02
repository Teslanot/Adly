from django import forms
from django.forms import ModelForm
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from add.models import Advertisement
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 

# # ModelForm----------------
# class Advforma(ModelForm): 
#     class Meta:
#         model = Advertisement
#         fields = ['title', 'descriptions', 'prices', 'auction', 'image']


#     def clean_title(self):
#         title = self.cleaned_data['title'] # извлек название из данных пользователя
#         if title.startswith('?'):# проверяю что начинеается с ?
#             raise ValidationError("Название не может начинаться с ?")
#         return title    # если не ? то возвращаю title обратно




# form = Advforma()
# AdverisementForm
# END -----------


# forms.Form---------------
class AdvertisementForm(forms.Form):
    # class="row mb-3 offset-sm-4"
    title       = forms.CharField(max_length=100, widget=forms.TextInput(
        {"class": "form-control-lg"}
    )) # validators работает, validators=[RegexValidator('[?+-/%]', inverse_match=True)]
    descriptions = forms.CharField(widget=forms.Textarea(
        {"class": "form-control-lg"}
    ))
    prices       = forms.DecimalField(widget=forms.NumberInput(
        {"class": "form-control-lg"}
    ))
    auction     = forms.BooleanField(required=False, widget=forms.CheckboxInput(
        {"class": "form-check-input"}
    )) # поле необязательное
    image       = forms.ImageField(required= False, widget=forms.FileInput(
        {"class": "form-control-lg"}
    ))

    title.widget.attrs.update({'class': 'special'})



    def clean_recipients(self):
        datab = self.cleaned_data['title']
        if "?" not in datab:
            raise ValidationError("?")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return datab
# END-----------------





