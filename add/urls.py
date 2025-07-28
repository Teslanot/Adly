from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, top_sellers, post_adv,post_adv_detail, add_to_favorites,remove_from_favorite,favorit_list, profile, edit_profile, delete_account, delete_adv ,ChangePasswordView, ResetPasswordView

urlpatterns = [
    path("", home, name = 'home'),
    path("top_sellers/", top_sellers, name='top_sellers'),
    path("post_adv/", post_adv, name='post_adv'),
    path("post_adv/<int:pk>", post_adv_detail, name='post_adv_detail'),
    path('add_to_favorites/<int:pk>/', add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorite/<int:pk>/', remove_from_favorite, name='remove_from_favorite'),
    path('favorites', favorit_list, name='favorit_list'),
    path('profile/', profile, name='profile'),
    path('profile/edit_profile/', edit_profile, name='edit_profile'),
    path('profile/delete_account/', delete_account, name='delete_account'),
    path('profile/adv/delete/<int:pk>/', delete_adv , name='delete_adv'),
    path('profile/password/', ChangePasswordView.as_view(), name='password_change'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'
    ), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ), name='password_reset_complete'),
]