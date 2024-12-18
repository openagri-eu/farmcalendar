import json
import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured
from django.contrib.messages import constants as messages
from dotenv import load_dotenv

from .env_helpers import get_env_var

load_dotenv()  # Load environment variables from .env file
from decouple import config, Csv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_ROOT = str(BASE_DIR / "static")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_var('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]']

EXTRA_ALLOWED_HOSTS = os.environ.get('EXTRA_ALLOWED_HOSTS', None)
if EXTRA_ALLOWED_HOSTS is not None:
    EXTRA_ALLOWED_HOSTS = EXTRA_ALLOWED_HOSTS.split(',')
    ALLOWED_HOSTS.extend(EXTRA_ALLOWED_HOSTS)

# Application definition
DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
]

LOCAL_APPS =[
    "farm_management.apps.FarmManagementConfig",
    "farm_activities.apps.FarmActivitiesConfig",
    "apis.apps.ApisConfig"
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'simple_history',
    'drf_spectacular',
    'crispy_forms',
    'crispy_bootstrap5',
]

INSTALLED_APPS = DEFAULT_APPS + LOCAL_APPS + THIRD_PARTY_APPS

GATEKEEPER_LOGIN_URL = os.environ.get('GATEKEEPER_LOGIN_URL', None)

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

if GATEKEEPER_LOGIN_URL == '':
    GATEKEEPER_LOGIN_URL = None

AUTHENTICATION_BACKENDS = (
    'farm_calendar.utils.auth_backends.CustomJWTAuthenticationBackend',
)
if GATEKEEPER_LOGIN_URL is None:
    AUTHENTICATION_BACKENDS = AUTHENTICATION_BACKENDS + ('django.contrib.auth.backends.ModelBackend',)


# AUTH_USER_MODEL = "harvesthand.DefaultAuthUserExtend"

# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = "calendar"

# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
LOGIN_URL = "login"


JWT_USER_ID_FIELD = 'user_id'
JWT_ALG = 'HS256'

# for HMAC this is the same as the verifying key
JWT_SIGNING_KEY = get_env_var('JWT_SIGNING_KEY')
JWT_COOKIE_NAME = get_env_var('JWT_COOKIE_NAME')
JWT_LOCAL_USER_ID_FIELD = os.environ.get('JWT_LOCAL_USER_ID_FIELD', 'username')
AUTO_CREATE_AUTH_USER = os.environ.get('AUTO_CREATE_AUTH_USER', 'True').lower() == 'true'

#lets igore RSA-based signing for now...
# with open(str(BASE_DIR / 'public.pem'), 'r') as f:
#     JWT_PUBLIC_KEY = f.read()
# with open(str(BASE_DIR / 'private.pem'), 'r') as f:
#     JWT_PRIVATE_KEY = f.read()

DEFAULT_API_VERSION = config('DEFAULT_API_VERSION', default='1.0.0')
SHORT_API_VERSION = f'v{DEFAULT_API_VERSION.split(".")[0]}'


REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_VERSION': SHORT_API_VERSION,
    'ALLOWED_VERSIONS': ['v1',],
    'VERSION_PARAM': 'version',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    'DEFAULT_RENDERER_CLASSES': [
        'apis.renderers.JSONLDRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'OpenAgri Farm Calendar API',
    'DESCRIPTION': 'API for farm assets and other farm related things.',
    'VERSION': DEFAULT_API_VERSION,
    'SERVE_INCLUDE_SCHEMA': True,
}



DEFAULT_OCSM_JSONLD_CONTEXT_FILE = (
    BASE_DIR / 'apis' / 'default_ocsm_context'
        / 'v0' / 'ocsm-profile-context.jsonld'
)

OCSM_JSONLD_CONTEXT_FILE = config('OCSM_JSONLD_CONTEXT_FILE', default=DEFAULT_OCSM_JSONLD_CONTEXT_FILE)

# with open(OCSM_JSONLD_CONTEXT_FILE, 'r') as f:
#     OCSM_JSONLD_CONTEXT = json.load(f)

# leave like this for now, it keeps response small and I dont really have
# full knowledge what I can add/remove from the full context
OCSM_JSONLD_CONTEXT  = {
  	"@context": [
	  	"https://w3id.org/ocsm/main-context.jsonld"
   	]
}

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'farm_calendar.utils.auth_middlewares.JWTAuthenticationMiddleware',
]

ROOT_URLCONF = 'farm_calendar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'farm_calendar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB'),
        'USER': os.getenv('POSTGRES_USER'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD'),
        'HOST': os.getenv('POSTGRES_HOST'),
        'PORT': os.getenv('POSTGRES_PORT', '5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# MESSAGE_TAGS setting maps Django's built-in message levels to CSS classes used by the front-end framework
# (e.g., Bootstrap).
# This allows messages from Django's messaging framework to be styled appropriately in the web interface.
MESSAGE_TAGS = {
    messages.DEBUG: "alert-info",
    messages.INFO: "alert-info",
    messages.SUCCESS: "alert-success",
    messages.WARNING: "alert-warning",
    messages.ERROR: "alert-danger",
}


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = str(BASE_DIR / "static_root")

STATICFILES_DIRS = [str(BASE_DIR / "static")]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

FIXTURE_DIRS = [(BASE_DIR / "fixtures")]



DEFAULT_CALENDAR_ACTIVITY_TYPES = {
    'fertilization': {
        'name': 'Fertilization',
        'description': 'Fertilization operation',
        "background_color": "#F5E8C7",
        "border_color": "#8B4513",
        "text_color": "#2F4F4F"
    },
    'irrigation': {
        'name': 'Irrigation',
        'description': 'Irrigation operation',
        'background_color': '#B3E5FC',
        'border_color': '#0288D1',
        'text_color': '#01579B'
    },
    'crop_protection':{
        'name': 'Pesticides',
        'description': 'Pesticide application',
        'background_color': '#C5E1A5',
        'border_color': '#8E7F2F',
        'text_color': '#4E342E',
    },
    'crop_stress_indicator':{
        'name': 'Crop Stress Indicator',
        'description': 'Crop Stress Indicator Observation',
        'background_color': '#FFCCCB',
        'border_color': '#C62828',
        'text_color': '#BF360C',
    },
    'crop_growth_stage':{
        'name': 'Crop Growth Stage Observation',
        'description': 'Crop Stress Indicator Observation',
        "background_color": "#F5E8C7",
        "border_color": "#8B4513",
        "text_color": "#2F4F4F"
    }
}