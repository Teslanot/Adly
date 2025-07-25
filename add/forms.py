from django import forms
from django.core.exceptions import ValidationError

class AdvertisementForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "w-full border border-gray-300 rounded-md p-3 focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Введите заголовок"
        })
    )

    descriptions = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "w-full border border-gray-300 rounded-md p-3 focus:outline-none focus:ring-2 focus:ring-blue-500",
            "rows": "5",
            "placeholder": "Опишите объявление"
        })
    )

    prices = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            "class": "w-full border border-gray-300 rounded-md p-3 focus:outline-none focus:ring-2 focus:ring-blue-500",
            "placeholder": "Введите цену"
        })
    )

    auction = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            "class": "h-5 w-5 text-blue-600 focus:ring-blue-500 border-gray-300 rounded"
        })
    )

    image = forms.ImageField(
        required=False,
        widget=forms.ClearableFileInput(attrs={
            "class": "w-full border border-gray-300 rounded-md p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
        })
    )

    def clean_recipients(self):
        datab = self.cleaned_data['title']
        if "?" not in datab:
            raise ValidationError("Заголовок должен содержать знак вопроса '?'")
        return datab