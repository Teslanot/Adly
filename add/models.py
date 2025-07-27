from django.db import models
from django.contrib import admin

from django.utils import timezone
from django.utils.html import format_html

from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from django.urls import reverse 

# главный
# venv/Scripts/activate   
# py manage.py makemigrations
# py manage.py migrate



User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.jpg')


class Advertisement(models.Model):
    title = models.CharField("Заголовок",max_length= 128)
    descriptions = models.TextField('Описание')
    prices = models.DecimalField(' Цена' , max_digits= 10 , decimal_places = 2)
    auction = models.BooleanField('Торг', help_text= 'Уместен ли торг')
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField("Изображения", upload_to='advertisements/')
    favorites = models.ManyToManyField(User, related_name='favorite_adv')

    def get_absolute_url(self):
        # post_adv/<int:pk>/
        # post_adv/self.pk/
        return reverse("post_adv_detail", kwargs={"pk": self.pk})


    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created == timezone.now().date():
            created_time =  self.created.strftime('%d.%m.%Y')
            return format_html(
                "<span style='color:green; font-weight: bold'>Сегодня {}</span>",
                created_time
            )
        return self.created.strftime('%d.%m.%Y')



    @admin.display(description='Дата обновления')
    def update_date(self):
        if self.update == timezone.now().date():
            update_time =  self.update.strftime('%d.%m.%Y')
            return format_html(
                "<span style='color:green; font-weight: bold'>Сегодня {}</span>",
                update_time
            )
        return self.update.strftime('%d.%m.%Y')

    @admin.display(description='Фото')
    def photo(self):
        if self.image:
           
            return format_html(
                "<img src = '{}' width='100px' heigth = '100px' ",
                self.image.url
            )
        return format_html(
                "<img src = 'http://127.0.0.1:8000/media/advertisements/no_image.jpg' width='100px' heigth = '100px' ",
                
            )


    def __str__(self) -> str:
        return f"Advertisement(id={self.id}, title={self.title}, price={self.prices}, created={self.created}, updated={self.update})"


    class Meta:
       db_table = 'Advertisement'