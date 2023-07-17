from django.shortcuts import render

from django.http import HttpResponse# класс для отправки ответа

# функция-представление
def lesson(request):
    return HttpResponse("ДЗ")