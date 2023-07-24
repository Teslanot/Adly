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






