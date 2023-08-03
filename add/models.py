from django.db import models

# Create your models here.








class User(models.Model):

    GENDER_CHOICE = [
        ('Ork', 'Ork'),
        ('Furri', 'Furri'),
        ('Iron', 'Iron'),


    ]



    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICE,max_length= 50, default='Ork')
    mail = models.EmailField()






class Advertisement(models.Model):
    title = models.CharField("Заголовок",max_length= 128)
    prices = models.DecimalField(' цена' , max_digits= 10 , decimal_places = 2)
    created = models.DateField(auto_now_add= True)
    descriptions = models.TextField('описание')
    update = models.DateField(auto_now= True)
    auction = models.BooleanField('merch', help_text= 'Уместен ли торг')

    def __str__(self) -> str:
        return f'Advertisements(id = {self.id}, title = {self.title}, prices = {self.prices})'


    class Meta:
       db_table = 'Advertisements'





# from add.models import Advertisement



# from django.db import connection
# connection.queries