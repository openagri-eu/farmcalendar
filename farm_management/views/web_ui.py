from urllib.parse import urlencode

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

import requests

from farm_calendar.utils.jwt_utils import get_user_id_from_token, get_token_from_jwt_request


def index_view(request):
    return render(request, 'index.html')


def post_authentication(request):
    auth_token = request.GET.get(settings.POST_AUTH_TOKEN_ATTRIBUTE, None)
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


@login_required
def logout_view(request):
    response  = redirect('login')
    if settings.GATEKEEPER_LOGOUT_API_URL is not None:
        token = get_token_from_jwt_request(request)
        payload = {
            'refresh': token
        }
        req = requests.post(settings.GATEKEEPER_LOGOUT_API_URL, json=payload)
        if req.status_code != 200:
            messages.error(request, 'Failed to logout current user at gatekeeper')
    response.delete_cookie(settings.JWT_COOKIE_NAME)
    logout(request)
    return response