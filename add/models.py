from django.db import models
from django.contrib import admin


from django.utils import timezone # для времени
from django.utils.html import format_html # для создания строки html 


from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model
from django.urls import reverse 



# class Cats(models.Model):
#     name = models.CharField(max_length=50)
#     age = models.IntegerField()
#     breed = models.CharField(max_length=50)




# главный

# venv/Scripts/activate   
# py manage.py makemigrations
# py manage.py migrate


# заголовок - описание - цена - дата создания - дата обновления - тогр
User = get_user_model()


class Advertisement(models.Model):
    title = models.CharField("Заголовок",max_length= 128)#validators=[RegexValidator('[?+-/%]', inverse_match=True)]
    descriptions = models.TextField('Описание')
    prices = models.DecimalField(' Цена' , max_digits= 10 , decimal_places = 2)
    auction = models.BooleanField('Торг', help_text= 'Уместен ли торг')
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) # если User буджет удален то все обьявления связанные с ним тоже будут удалены
    image = models.ImageField("Изображения", upload_to='advertisements/')
    favorites = models.ManyToManyField(User, related_name='favorite_adv')

    def get_absolute_url(self):
        # post_adv/<int:pk>/
        # post_adv/self.pk/
        return reverse("post_adv_detail", kwargs={"pk": self.pk})# pk тоже самое что и id в модели


    #метод если запись была создана сегодня то мы отобразим ее зеленым цветом, если не сегодня , то серым
    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created == timezone.now().date():#проверяю что запись была создана сегодня
            created_time =  self.created.strftime('%d.%m.%Y') # 19:30:15 at %H:%M:%S
            return format_html(
                "<span style='color:green; font-weight: bold'>Сегодня {}</span>",
                created_time
            )
        return self.created.strftime('%d.%m.%Y') # 04.08.2023 at 19:30:15 at %H:%M:%S



    @admin.display(description='Дата обновления')
    def update_date(self):
        if self.update == timezone.now().date():#проверяю что запись была создана сегодня
            update_time =  self.update.strftime('%d.%m.%Y') # 19:30:15 at %H:%M:%S
            return format_html(
                "<span style='color:green; font-weight: bold'>Сегодня {}</span>",
                update_time
            )
        return self.update.strftime('%d.%m.%Y') # 04.08.2023 at 19:30:15 at %H:%M:%S

    @admin.display(description='Фото')
    def photo(self):
        if self.image:#проверяю что есть картинка
           
            return format_html(
                "<img src = '{}' width='100px' heigth = '100px' ",
                self.image.url
            )
        return format_html(
                "<img src = 'http://127.0.0.1:8000/media/advertisements/no_image.jpg' width='100px' heigth = '100px' ",
                
            )



    # представление в виде строки 
    def __str__(self) -> str:
        return f"Advertisement(id={self.id}, title={self.title}, price={self.prices}, created={self.created}, updated={self.update})"
    
    

    #работы с самой таблице


    class Meta:
       db_table = 'Advertisement'





#         from app_advertisements.models import Advertisements                                
#         adv1 = Advertisements (title = 'Молоко', descriptoin = 'Свежее молоко', price = 100, auction = True)   # создаю запись                           
#         adv1.save()           #сохраняю                      
#                                       
# from django.db import connection                              
# connection.queries     # получаю все запросы к sql                            
#                                       
                               