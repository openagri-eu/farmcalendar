from urllib.parse import urlencode

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# from farm_calendar.utils.jwt_utils import get_user_id_from_jwt_request
# from farm_calendar.utils.auth_decorators import jwt_required

@login_required
def index_view(request):
    return render(request, 'index.html')


def login_view(request):
    if settings.GATEKEEPER_LOGIN_URL is not None:
        redirect_back_param = {'next': 'farm_calendar'}
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