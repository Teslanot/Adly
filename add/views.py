from django.shortcuts import render,redirect # для того чтобы отдавать html
from django.urls import reverse #получение ссылки по названию в urls
from .models import Advertisement
# from .forms import AdverisementForm
from .forms import AdvertisementForm
from django.db.models import Count
from django.contrib.auth import get_user_model
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required # если пользователь не авторизован перенаправляем его
from django.urls import reverse_lazy # как reverse но только ленивая функция
from datetime import datetime , timedelta
from django.utils import timezone



# функции-представления
# <!-- {{}}  - это переменная -->
# <!-- {% %}  - это блоки с функционалом -->
# <!-- {% if else while for %}  - это блоки с функционалом -->
User = get_user_model()


def home(request: WSGIRequest):
    title = request.GET.get('query')
    if title: # если пользователь что-то ищет
        datab = Advertisement.objects.filter(title__icontains = title) # SELECT * FROM Advertisement WHERE title = title
    else: # если ничего не ищет(просто все обьявления)
        datab = Advertisement.objects.all() # беру все записи из БД


    context = {'advertisements' : datab, 'title': title} # словарь
    return render(request, 'index.html', context)




def top_sellers(request):
    users = User.objects.annotate(
        adv_count = Count('advertisement')# записываю в  adv_count колисчество обьявлений у каждого пользователя
    ).order_by('-adv_count') # сортировка от наибольшего к наименьшему

    context = {"users" : users}
    return render(request, 'top-sellers.html', context)




def post_adv_detail(request: WSGIRequest, pk):
    # post_adv/<int:pk>/
    # http://127.0.0.1:8000/post_adv/1/
    # pk = 1
    adv = Advertisement.objects.get(id = pk) # ищу запись по id
    context = {"adv" : adv}
    return render(request, 'advertisement.html', context)

# advertisements

# AdvForma
def post_adv(request: WSGIRequest):
    
    print('request.GET',request.GET)
    print('request.POST',request.POST)
    print('request.FILES',request.FILES)
    print('request.user',request.user)

    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES) # передаю данные с запроса на проверку 
        if form.is_valid(): # True/False  проверяю правильность
            # print(request.POST['title'])
            print(form.cleaned_data) # отдает словарь со всеми данными
            adv = Advertisement(**form.cleaned_data) # распаковка словаря
            adv.user = request.user # отдельно указал пользователя 
            adv.save()  # сохраняю запись
            return redirect(
                reverse('home') # переадресация на главную страницу 
            )

        else: # если неправильно
            print(form.errors) # вывожу эту ошибку


    else: # GET или другие
        form = AdvertisementForm() # пустая форма

    context = {'form' : form} # словарь
    return render(request, 'advertisement-post.html', context)


def test(request):
    return render(request, 'test.html')

def test2(request):
    return render(request, 'test2.html')




# def novinki(request:WSGIRequest):
#     title = request.GET.get('query')
#     if title: # если пользователь что-то ищет
#         data = Advertisement.objects.filter(title__icontains = title) # SELECT * FROM Advertisement WHERE title = title
#     else: # если ничего не ищет(просто все обьявления)
#         data = Advertisement.objects.all() # беру все записи из БД
#     context = {'advertisements' : data, 'title': title}
#     return render(request, 'novinki.html', context)


# def adv_filter(request,pk):
#     adv_filter = Advertisement.objects.all()
#     if pk == 1:
#         now =  datetime.now() - timedelta(minutes= 60*24*7)
#         adv_filter = adv_filter.filter(created__gte=now)
#         adv_filter = adv_filter
#     elif pk == 2:
#         now =  datetime.now() - timedelta(minutes= 60*24*30)
#         adv_filter = adv_filter.filter(created__gte=now)
#     elif pk == 3:
#         adv_filter = adv_filter
#     return render(request, 'novinki.html', {'adv_filter':adv_filter})