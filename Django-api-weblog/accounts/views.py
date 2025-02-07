from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserCreationForm, UserLoginForm
from .models import Profile
from django.contrib.auth import logout

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # ایجاد پروفایل کاربر
            login(request, user)  # لاگین کاربر
            return redirect('profile')  # صفحه پروفایل
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # صفحه پروفایل
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})


def logout_user(request):
    logout(request)
    return redirect('login')