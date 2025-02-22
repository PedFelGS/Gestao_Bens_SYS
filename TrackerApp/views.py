from django.shortcuts import render, redirect
from assets_TrackerApp.models import Assets, Categories
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'pages/home.html', {
        "is_home": True
    })

@login_required
def user_profile(request):
    return render(request, 'pages/user_profile.html')

def custom_page_not_found(request, exception):
    return render(request, '404.html', {}, status=404)

def custom_error(request):
    return render(request, '500.html', {}, status=500)