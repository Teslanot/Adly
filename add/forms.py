from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import Profile, Comment

User = get_user_model()

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
    def clean_prices(self):
        price = self.cleaned_data.get('prices')
        if price is not None and price < 0:
            raise ValidationError("Цена не может быть отрицательной.")
        return price

    def clean_recipients(self):
        datab = self.cleaned_data['title']
        if "?" not in datab:
            raise ValidationError("Заголовок должен содержать знак вопроса '?'")
        return datab


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full pl-10 pr-4 py-3 bg-white/80 backdrop-blur-sm border-2 border-gray-200 rounded-xl focus:border-blue-500 focus:ring-4 focus:ring-blue-100 transition-all duration-300 placeholder-gray-400 text-sm',
                'placeholder': 'Имя',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full pl-10 pr-4 py-3 bg-white/80 backdrop-blur-sm border-2 border-gray-200 rounded-xl focus:border-blue-500 focus:ring-4 focus:ring-blue-100 transition-all duration-300 placeholder-gray-400 text-sm',
                'placeholder': 'Фамилия',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full pl-10 pr-4 py-3 bg-white/80 backdrop-blur-sm border-2 border-gray-200 rounded-xl focus:border-blue-500 focus:ring-4 focus:ring-blue-100 transition-all duration-300 placeholder-gray-400 text-sm',
                'placeholder': 'Email',
            }),
        }

class AvatarUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'w-full pl-4 pr-4 py-3 bg-white/80 backdrop-blur-sm border-2 border-gray-200 rounded-xl focus:border-blue-500 focus:ring-4 focus:ring-blue-100 transition-all duration-300 placeholder-gray-400 text-sm'
            })


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'parent']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Напишите комметарий...',
                'class': 'w-full p-2 border round'
            })
        }
    parent = forms.ModelChoiceField(
        queryset=Comment.objects.all(),
        required=False,
        widget=forms.HiddenInput()
    )