from django.urls import path
from .views import profile , login_view,logout_view,register

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('sign_in/', register, name='sign_in'),
    
]