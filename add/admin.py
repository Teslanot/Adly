from django.contrib import admin
from .models import Advertisement # импортирую свою модель
# класс обьекта модели для подсказки
from django.db.models.query import QuerySet

# py manage.py createsuperuser - создания аккаунта супер пользователя
# пароль не отображается
# http://127.0.0.1:8000/admin

# кастомный класс для модели
class AdvertisementsAdmin(admin.ModelAdmin):
    list_display  = ['id', 'title','descriptions','prices','auction', 'created_date', 'update_date','photo'] # какие поля должны отображатья в таблице
    list_filter = ['auction', 'created'] # поля по которыфм  можно  сделать фильтрацию
    actions = ['make_auction_as_false','make_auction_as_true'] # спискок функций для выбранных элементов
    search_fields = ['title']
    date_hierarchy = 'created'
    fieldsets = ( # указание разделов для полей записи
        ('Общее', { # название раздела 1
            "fields": (
                'title','descriptions','user','image' # поля раздела
            ),
        }),
        ('Фианансы', { # название раздела 2
            "fields": (
                'prices','auction'
            ),
            'classes':['collapse'] # функция скрытия раздела
        }),
    )
    





    @admin.action(description='Убрать возможность торга')
    def make_action_as_false(self, request, queryset:QuerySet):
        queryset.update(auction = False) # обновить значение auction у выбранных записей на False


    @admin.action(description='Добавить возможность торга')
    def make_action_as_true(self, request, queryset:QuerySet):
        queryset.update(auction = True) # обновить значение auction у выбранных записей на False








# подключение модели в админку и кастомной модели
admin.site.register(Advertisement, AdvertisementsAdmin)


# def add_list(some_list : list):
#     some_list.append()

# add_list()













