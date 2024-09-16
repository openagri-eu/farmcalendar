from django.contrib.auth import authenticate

from farm_calendar.utils.jwt_utils import get_token_from_jwt_request

class JWTAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = get_token_from_jwt_request(request)
        user = authenticate(request, token=token)
        if user:
            request.user = user

        response = self.get_response(request)
        return response
