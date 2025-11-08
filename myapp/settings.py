import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#create media folder/directory 
MEDIA_URL="/media/"
MEDIA_ROOT=os.path.join(BASE_DIR,"media/")

#static media/files
STATICFILES_DIRS=[os.path.join(PROJECT_DIR,"frontend/")]
STATIC_ROOT=os.path.join(BASE_DIR,"static/")
STATIC_URL="/static/"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nn4=_bzv!i_b65--t*w77wqh8hjxha)#yz(=2ef8v--g51!uy-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'allauth',
    'feed',
    'allauth.account',
    'allauth.socialaccount',
    'tailwind',
    'theme',
    'profiles',
    'sorl.thumbnail',
    'followers',
    
]
if DEBUG:
    INSTALLED_APPS+= ["django_browser_reload"]



TAILWIND_APP_NAME='theme'


NPM_BIN_PATH="C:\\Program Files\\nodejs\\npm.cmd"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'allauth.account.middleware.AccountMiddleware'
]

if DEBUG:
    
    MIDDLEWARE+= [
        "django_browser_reload.middleware.BrowserReloadMiddleware"
    ]

ROOT_URLCONF = 'myapp.urls'

#create template directory


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(PROJECT_DIR,'myapp/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

#add new django all auth settings
SITE_ID=1                                   #for the one site we have
LOGIN_URL="/login/"                         #login url
LOGIN_REDIRECT_URL="/"                      #redirect to homepage after login
ACCOUNT_AUTHENTICATION_METHOD="email"     #authenticate using an email address
ACCOUNT_CONFIRM_EMAIL_ON_GET= True          #allow user to authenticate from email link
ACCOUNT_EMAIL_REQUIRED=True                 #requires user to have an email
ACCOUNT_EMAIL_VERIFICATION="optional"       #does the site require the user to verify email? can be set to mandatory
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION=True    #login when email has been confirmed
ACCOUNT_LOGOUT_ON_GET=True                  #logout without the need to fill out a form
ACCOUNT_LOGIN_ON_PASSWORD_RESET=True        
ACCOUNT_LOGOUT_REDIRECT="/"                 #redirect user to homepage when they log out
ACCOUNT_PRESERVE_USERNAME_CASING=False      #Usernames are not case sensitive.THATO is the same as thato
ACCOUNT_SESSION_REMEMBER=True               #remembers user forever
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE=True    #to prevent user ffrom locking themselves out if they mistype their password
ACCOUNT_USERNAME_MIN_LENGTH=2               #minimun username length accepted

#add authenticationbackend

AUTHENTICATION_BACKENDS=[ 
    
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend"

]

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

