from urllib.parse import urlencode

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect


def index_view(request):
    return render(request, 'index.html')


def post_authentication(request):
    auth_token = request.GET.get('auth_token', None)
    user = authenticate(request, token=auth_token)
    response = None
    if user is not None:
        next = settings.LOGIN_REDIRECT_URL
        response = redirect(f"{next}")
        response.set_cookie(settings.JWT_COOKIE_NAME, auth_token)
    else:
        response = HttpResponse('Unauthorized', status=401)
    return response


def login_view(request):
    if settings.GATEKEEPER_LOGIN_URL is not None:
        redirect_back_param = {'next': 'FarmCalendar'}
        url_with_param = f"{settings.GATEKEEPER_LOGIN_URL}?{urlencode(redirect_back_param)}"
        return redirect(url_with_param)
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