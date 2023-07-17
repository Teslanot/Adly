from django.urls import path

# импортирую свои представления

from .views import home, test, test2, top_sellers

#  маршрутизатор приложения




urlpatterns = [
    path("", home, name = 'home'), # главная страница 
    path("top_sellers", top_sellers, name='top_sellers'), # топ продавцов 
    path("test/", test, name = 'test'), 
    path("test2/", test2, name = 'test2'), 
]   



# для того чтобы отобразить html:
# 1 создать html
# 2 создать функцию представление в views.py
# 3 создать ссылку в urls.py по которой будет вызывать эта функция