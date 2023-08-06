from django.contrib import admin
from .models import Advertisement # импортирую свою модель
# класс обьекта модели для подсказки
from django.db.models.query import QuerySet

# py manage.py createsuperuser - создания аккаунта супер пользователя
# пароль не отображается
# http://127.0.0.1:8000/admin

# кастомный класс для модели
class AdvertisementsAdmin(admin.ModelAdmin):
    list_display  = ['id', 'title','descriptions','prices','auction', 'created_date', 'update_date'] # какие поля должны отображатья в таблице
    list_filter = ['auction', 'created'] # поля по которыфм  можно  сделать фильтрацию
    actions = ['make_auction_as_false','make_auction_as_true'] # спискок функций для выбранных элементов
    fieldsets = ( # указание разделов для полей записи
        ('Общее', { # название раздела 1
            "fields": (
                'title','descriptions' # поля раздела
            ),
        }),
        ('Фианансы', { # название раздела 2
            "fields": (
                'prices','auction'
            ),
            'classes':['collapse'] # функция скрытия раздела
        }),
    )
    





    # функции для выбранных элементов
    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self,request,queryset:QuerySet): #queryset записи которые мы выбрали
        queryset.update(auction = False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self,request,queryset:QuerySet):
        queryset.update(auction = True)






# регистрирую модели и 
admin.site.register(Advertisement, AdvertisementsAdmin)


# def add_list(some_list : list):
#     some_list.append()

# add_list()













