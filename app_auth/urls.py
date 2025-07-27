from django.urls import path
from .views import login_view,logout_view,register

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('sign_in/', register, name='sign_in'),
]