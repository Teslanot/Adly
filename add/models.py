from django.db import models

        # модули для настройки методов админки
from django.contrib import admin
from django.utils import timezone # для времени
from django.utils.html import format_html # для создания строки html
        #

# Create your models here.
# тестовый класс



class User(models.Model):

    GENDER_CHOICE = [
        ('Ork', 'Ork'),
        ('Furri', 'Furri'),
        ('Iron', 'Iron'),
    ]



class Cats(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    breed = models.CharField(max_length=50)







# главный

# venv/Scripts/activate   
# py manage.py makemigrations
# py manage.py migrate
# заголовок - описание - цена - дата создания - дата обновления - тогр


class Advertisement(models.Model):
    title = models.CharField("Заголовок",max_length= 128)
    prices = models.DecimalField(' цена' , max_digits= 10 , decimal_places = 2)
    created = models.DateField(auto_now_add= True)
    descriptions = models.TextField('описание')
    update = models.DateField(auto_now= True)
    auction = models.BooleanField('merch', help_text= 'Уместен ли торг')

    def __str__(self) -> str:
        return f'Advertisements(id = {self.id}, title = {self.title}, prices = {self.prices})'


    class Meta:
       db_table = 'Advertisements'

    #если запись была создана сегодня то она будет зеленого цвета
    @admin.display(description='дата создания')
    def created_date(self):
        if self.created == timezone.now().date():#проверяю что запись была создана сегодня
            created_time = self.created.strftime('%H:%M:%S') #формат 17:14:25
            return format_html(
                '<span style="color:green; font-weight:bold">сегодня в {}</span>',created_time
            )
        return self.created.strftime('%d.%m.%Y at %H:%M:%S') #формат 03.08.2023 at 17:14:25



    #если запись была создана сегодня то она будет зеленого цвета
    @admin.display(description='дата обновления')
    def update_date(self):
        if self.update == timezone.now().date():#проверяю что запись была создана сегодня
            update_time = self.update.strftime('%H:%M:%S') #формат 17:14:25
            return format_html(
                '<span style="color:green; font-weight:bold">сегодня в {}</span>',update_time
            )
        return self.update.strftime('%d.%m.%Y at %H:%M:%S') #формат 03.08.2023 at 17:14:25









#         from app_advertisements.models import Advertisements                                
#         adv1 = Advertisements (title = 'Молоко', descriptoin = 'Свежее молоко', price = 100, auction = True)   # создаю запись                           
#         adv1.save()           #сохраняю                      
#                                       
# from django.db import connection                              
# connection.queries     # получаю все запросы к sql                            
#                                       
                               