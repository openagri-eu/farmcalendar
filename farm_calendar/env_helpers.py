import os
from django.core.exceptions import ImproperlyConfigured


def get_env_var(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        raise ImproperlyConfigured(f'"{var_name}" was not set as an env variable.')
