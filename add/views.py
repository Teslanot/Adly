from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse
from .models import Advertisement
from .forms import AdvertisementForm
from django.db.models import Count
from django.contrib.auth import get_user_model
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from datetime import datetime, timedelta
# from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


User = get_user_model()


def home(request: WSGIRequest):
    title = request.GET.get('query')
    if title:
        data = Advertisement.objects.filter(title__icontains = title)
    else:
        data = Advertisement.objects.all()
    
    today = datetime.now().date()
    week_ago = today - timedelta(days=7)

    daily_ads = Advertisement.objects.filter(created=today)[:10]
    weekly_ads = Advertisement.objects.filter(created=week_ago)[:10]

    context = {
        'advertisements': data,
        'title': title,
        'daily_ads': daily_ads,
        'weekly_ads': weekly_ads,
    }
    return render(request, 'index.html', context)

def top_sellers(request):
    users = User.objects.annotate(
        adv_count = Count('advertisement')
    ).order_by('-adv_count')

    context = {"users" : users}
    return render(request, 'top-sellers.html', context)



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
    return render(request, 'all-fav.html', context)




def post_adv_detail(request: WSGIRequest, pk):
    # post_adv/<int:pk>/
    adv = Advertisement.objects.get(id = pk)
    context = {"adv" : adv}
    return render(request, 'advertisement.html', context)


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
    return render(request, 'advertisement-post.html', context)