# маршрутизатор приложения
from django.urls import path

from .views import profile , login_view,logout_view,sign_in



urlpatterns = [
    path('profile/', profile, name='profile'), # http://127.0.0.1:8000/auth/profile/
    path('login/', login_view, name='login'), # http://127.0.0.1:8000/auth/profile/
    path('logout/', logout_view, name='logout'), # http://127.0.0.1:8000/auth/profile/
    path('sign_in/', sign_in, name='sign_in'), # http://127.0.0.1:8000/auth/profile/
    
]
#    16:40 - 16:50