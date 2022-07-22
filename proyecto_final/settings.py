"""
Archivo Base de configuracion para que hereden todos los entornos
"""

from pathlib import Path

from unipath import Path
import environ
import django_heroku
#BASE_DIR = Path(__file__).resolve().parent.parent


BASE_DIR = Path(__file__).ancestor(2)
"""Con esta linea de codigo digo que el directorio base va a ser el mismo pero ahora trabajamos bajo unipath y no por os (que es el que usa por defecto django)."""
print(BASE_DIR)
#environ init
env = environ.Env( SECRET_KEY = str, )


# read th .env file
environ.Env.read_env('.env')    

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env('DJANGO_SECRET_KEY')
from django.core.exceptions import ImproperlyConfigured
def get_env_variable(var_name):
    try:
        return env(var_name)
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

SECRET_KEY = get_env_variable('SECRET_KEY')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #extras
    'location_field.apps.DefaultConfig',
    #third party apps
    'ckeditor',
    "crispy_bootstrap5",
    'crispy_forms',
    
    #local apps
    'applications.jugador',
    'applications.busqueda',
    'applications.categoria',

]


CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyecto_final.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.child('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'proyecto_final.wsgi.application'



# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

"""Mi modelo para usuarios se encuentra en app Jugador y se llama User"""
#AUTH_USER_MODEL = 'jugador.User'


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL= '/pagina-principal/'

django_heroku.settings(locals())

import os



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG') 



ALLOWED_HOSTS = env('ALLOWED_HOSTS').split( )
    




DATABASES = {
    'default': {
        #voy a trabajar con postgresql en vez de sqlite
        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': os.path.join(BASE_DIR,'db.sqlite3'),
    }
}

"""Le digo a django que dentro de la carpeta static voy a tener mis archivos estaticos"""
STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR.child('static')]
STATICFILES_DIRS = (BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


#le digo que la url de la imagen se genere dominio/media/..
MEDIA_URL = '/media/'
#carpeta raiz donde va a etsar almacenado todos los archivos multimedia
#busca la carpeta llamada media
MEDIA_ROOT = BASE_DIR.child('media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'