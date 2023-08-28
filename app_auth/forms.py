
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 


# Register
class CustomUserCreationForm(UserCreationForm): 
    class Meta: 
        model =  User
        fields = ('password','username','first_name','last_name','email') 

# End REGISTRATION --------------------------------