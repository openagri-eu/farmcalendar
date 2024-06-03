from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next = settings.LOGIN_REDIRECT_URL
            return redirect(f"{next}")
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'auth/login.html')