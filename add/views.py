from django.contrib import messages
from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.urls import reverse_lazy

from .models import Advertisement
from .models import Profile
from .models import Comment
from .forms import AdvertisementForm, ProfileUpdateForm, AvatarUpdateForm, CustomPasswordChangeForm, CommentForm

from django.db.models import Count
from django.contrib.auth import get_user_model
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordChangeView

from datetime import datetime, timedelta
import random

from django.http import JsonResponse

from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


User = get_user_model()

def home(request):
    title = request.GET.get('query')
    if title:
        data = Advertisement.objects.filter(title__icontains=title)
    else:
        data = Advertisement.objects.all().order_by('-created')
    
    paginator = Paginator(data, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    today = datetime.now().date()
    week_ago = today - timedelta(days=7)

    daily_ads = Advertisement.objects.filter(created=today)[:10]
    weekly_ads = Advertisement.objects.filter(created=week_ago)[:10]

    all_ads = Advertisement.objects.all()
    
    if all_ads.exists():
        if all_ads.count() >= 3:
            carousel_ads = random.sample(list(all_ads), 3)
        else:
            carousel_ads = list(all_ads)
            remaining_slots = 3 - len(carousel_ads)
            
            default_items = [
                {
                    'title': 'Digital Prism',
                    'description': 'Where geometry meets art in a stunning display of light and form.',
                    'image': 'static/img/adv.png',
                    'is_default': True
                },
                {
                    'title': 'Tech Haven', 
                    'description': 'Immerse yourself in the cutting edge of technology and innovation.',
                    'image': 'static/img/adv.png',
                    'is_default': True
                },
                {
                    'title': 'Neural Dreams',
                    'description': 'AI-generated masterpieces that blur the line between human and machine creativity.',
                    'image': 'static/img/adv.png', 
                    'is_default': True
                }
            ]
            
            carousel_ads.extend(default_items[:remaining_slots])

    context = {
        'page_obj': page_obj,
        'daily_ads': daily_ads,
        'weekly_ads': weekly_ads,
        'title': title,
        'carousel_ads': carousel_ads,
    }
    return render(request, 'main/index.html', context)

def top_sellers(request):
    users = User.objects.annotate(
        adv_count = Count('advertisement')
    ).order_by('-adv_count')

    context = {"users" : users}
    return render(request, 'main/top-sellers.html', context)



@login_required
@require_POST
def add_to_favorites(request, pk):
    adv = get_object_or_404(Advertisement, id=pk)
    adv.favorites.add(request.user)
    return JsonResponse({"success": True, "action": "added"})

@login_required
@require_POST
def remove_from_favorite(request, pk):
    adv = get_object_or_404(Advertisement, id=pk)
    adv.favorites.remove(request.user)
    return JsonResponse({"success": True, "action": "removed"})


@login_required
def favorit_list(request):
    user = request.user
    favorites = user.favorite_adv.all()
    context = {"favorite_list": favorites}
    return render(request, 'actions/all-fav.html', context)




def post_adv_detail(request: WSGIRequest, pk):
    # post_adv/<int:pk>/
    adv = get_object_or_404(Advertisement, id=pk)
    comments = adv.comments.filter(parent__isnull=True).select_related('author__profile').prefetch_related('replies__author__profile')


    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.adv = adv
            comment.author = request.user
            comment.save()
            return redirect('post_adv_detail', pk=pk)
    else:
        form = CommentForm()

    context = {
        'adv': adv,
        'comments': comments,
        'form': form
    }
    return render(request, 'main/advertisement.html', context)


def post_adv(request: WSGIRequest):
    
    print('request.GET',request.GET)
    print('request.POST',request.POST)
    print('request.FILES',request.FILES)
    print('request.user',request.user)

    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            
            print(form.cleaned_data)
            adv = Advertisement(**form.cleaned_data)
            adv.user = request.user
            adv.save()
            return redirect(
                reverse('home')
            )

        else:
            print(form.errors)


    else:
        form = AdvertisementForm()

    context = {'form' : form}
    return render(request, 'actions/advertisement-post.html', context)

@login_required
def profile(request):
    user = request.user
    adv_list = Advertisement.objects.filter(user=user).order_by('-created')
    adv_count = adv_list.count()
    
    context = {
        "adv_list": adv_list,
        "adv_count": adv_count,
        "user": user
    }
    return render(request, 'profile/profile.html', context)



@login_required
def edit_profile(request):
    user = request.user

    profile, created = Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = ProfileUpdateForm(request.POST, instance=user)
        avatar_form = AvatarUpdateForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and avatar_form.is_valid():
            user_form.save()
            avatar_form.save()
            return redirect('profile')
    else:
        user_form = ProfileUpdateForm(instance=user)
        avatar_form = AvatarUpdateForm(instance=profile)

    return render(request, 'profile/edit_profile.html', {
        'user_form': user_form,
        'avatar_form': avatar_form,
    })

@login_required
def delete_account(request):
    user = request.user
    if request.method == 'POST':
        user.delete()
        logout(request)
        return redirect('home')

@login_required
@require_POST
def delete_adv(request, pk):
    if not request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({"success": False, "message": "Неверный запрос"}, status=400)

    adv = get_object_or_404(Advertisement, id=pk, user=request.user)
    adv.delete()
    return JsonResponse({"success": True})

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'profile/change_password.html'
    success_message = "Ваш пароль успешно изменен"
    success_url = reverse_lazy('profile')

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'profile/password_reset.html'
    email_template_name = 'profile/password_reset_email.html'
    subject_template_name = 'profile/password_reset_subject.txt'
    success_message = (
        "Инструкция по сбросу пароля отправлена, если такой email существует в системе."
    )
    success_url = reverse_lazy('home')