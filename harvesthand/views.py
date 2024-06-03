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
            return redirect(f"{settings.LOGIN_URL}?next={request.path}")
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'auth/login.html')