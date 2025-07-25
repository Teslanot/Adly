from django.urls import path

from .views import home, top_sellers, post_adv,post_adv_detail, add_to_favorites,remove_from_favorite,favorit_list

urlpatterns = [
    path("", home, name = 'home'),
    path("top_sellers/", top_sellers, name='top_sellers'),
    path("post_adv/", post_adv, name='post_adv'),
    path("post_adv/<int:pk>", post_adv_detail, name='post_adv_detail'),
    path('add_to_favorites/<int:pk>/', add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorite/<int:pk>/', remove_from_favorite, name='remove_from_favorite'),
    path("favorites", favorit_list, name='favorit_list'),
]