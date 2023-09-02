from django.urls import path

# импортирую свои представления

from .views import home, test, test2, top_sellers, post_adv,post_adv_detail, novinki
#  маршрутизатор приложения adv_filter




urlpatterns = [
    path("", home, name = 'home'), # главная страница 
    path("top_sellers/", top_sellers, name='top_sellers'), # топ продавцов 
    path("post_adv/", post_adv, name='post_adv'),
    path("post_adv/<int:pk>", post_adv_detail, name='post_adv_detail'),
    path("test/", test, name = 'test'), 
    path("test2/", test2, name = 'test2'), 
    path("novinki/", novinki, name = 'novinki'), 
    # path("adv_filter/<int:pk>", adv_filter, name='adv_filter'),
]       



# для того чтобы отобразить html:
# 1 создать html
# 2 создать функцию представление в views.py
# 3 создать ссылку в urls.py по которой будет вызывать эта функция