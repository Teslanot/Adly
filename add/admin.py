from django.contrib import admin
from .models import Advertisement

from django.db.models.query import QuerySet

class AdvertisementsAdmin(admin.ModelAdmin):
    list_display  = ['id', 'title','descriptions','prices','auction', 'created_date', 'update_date','photo']
    list_filter = ['auction', 'created']
    actions = ['make_auction_as_false','make_auction_as_true']
    search_fields = ['title']
    date_hierarchy = 'created'
    fieldsets = (
        ('Общее', {
            "fields": (
                'title','descriptions','user','image'
            ),
        }),
        ('Фианансы', {
            "fields": (
                'prices','auction'
            ),
            'classes':['collapse']
        }),
    )
    

    @admin.action(description='Убрать возможность торга')
    def make_action_as_false(self, request, queryset:QuerySet):
        queryset.update(auction = False)

    @admin.action(description='Добавить возможность торга')
    def make_action_as_true(self, request, queryset:QuerySet):
        queryset.update(auction = True)








# подключение модели в админку и кастомной модели
admin.site.register(Advertisement, AdvertisementsAdmin)


# def add_list(some_list : list):
#     some_list.append()

# add_list()













