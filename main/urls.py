"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# path - для создания ссылки
# include - для подколючения маршпрутизаторов приложения

# импортирую свои представления
from lesson_4.views import lesson


# главный маршрутизатор

# создали приложение py manage.py startapp lesson_4
# подключили приложение в настройках
# создали функцию в views.py
# в главном маршрутизаторе urls.py импортировали эту функцию 
# и создали ссылку



urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('add.urls')), # подключил марштрутизатор приложения add
    path("lesson_4/", lesson)
]   
