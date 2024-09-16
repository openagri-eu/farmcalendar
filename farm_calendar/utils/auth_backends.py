from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

from farm_calendar.utils.jwt_utils import get_user_id_from_token

class CustomJWTAuthenticationBackend(BaseBackend):
    def authenticate(self, request, token, **kwargs):
        user_id = get_user_id_from_token(token)
        if not user_id:
            return None

        user = self.get_user(user_id)
        if user is not None:
            return user

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(**{settings.JWT_LOCAL_USER_ID_FIELD: user_id})
        except User.DoesNotExist:
            if settings.AUTO_CREATE_AUTH_USER:
                password = User.objects.make_random_password()
                new_user = User.objects.create_user(**{
                    settings.JWT_LOCAL_USER_ID_FIELD: user_id,
                    'email': f'{user_id}@farm.calendar',
                    'password': password
                })
                try:
                    new_user.save()
                except Exception:
                    pass
                else:
                    return new_user
            return None
