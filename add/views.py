from django.shortcuts import render,redirect # для того чтобы отдавать html
from django.urls import reverse #получение ссылки по названию в urls
from .models import Advertisement
from .forms import AdverisementForm
from django.core.handlers.wsgi import WSGIRequest



# функции-представления
# <!-- {{}}  - это переменная -->
# <!-- {% %}  - это блоки с функционалом -->
# <!-- {% if else while for %}  - это блоки с функционалом -->

def home(request):
    data = Advertisement.objects.all() # беру все записи из БД
    context = {'advertisements' : data} # словарь
    return render(request, 'index.html', context)





def post_adv(request: WSGIRequest):
    
    print('request.GET',request.GET)
    print('request.POST',request.POST)
    print('request.FILES',request.FILES)
    print('request.user',request.user)

    if request.method == "POST":
        form = AdverisementForm(request.POST, request.FILES) # передаю данные с запроса на проверку 
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
        form = AdverisementForm() # пустая форма



    # if request.method == "POST":
    #     form =Forma(request.POST, request.FILES) # передаю данные с запроса на проверку 
    #     if form.is_valid(): # True/False  проверяю правильность
    #         # print(request.POST['title'])
    #         print(form.cleaned_data) # отдает словарь со всеми данными
    #         adv = Advertisement(**form.cleaned_data) # распаковка словаря
    #         adv.user = request.user # отдельно указал пользователя 
    #         adv.save()  # сохраняю запись
    #         return redirect(
    #             reverse('home') # переадресация на главную страницу 
    #         )

    #     else: # если неправильно
    #         print(form.errors) # вывожу эту ошибку


    # else: # GET или другие
    #     form = AdverisementForm() # пустая форма

    context = {'form' : form} # словарь
    return render(request, 'advertisement-post.html', context)


# def index(request):
#     context = {'advertisements': {ad}}
def top_sellers(request):
    return render(request, 'top-sellers.html')

def test(request):
    return render(request, 'test.html')

def test2(request):
    return render(request, 'test2.html')