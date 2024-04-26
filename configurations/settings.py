"""
Django settings for configurations project.

Generated by "django-admin startproject" using Django 5.0.

For more information on this file, see https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see https://docs.djangoproject.com/en/5.0/ref/settings/
"""


from pathlib import Path
from django.urls import reverse_lazy

import os


#Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent


#Quick-start development settings - unsuitable for production
#See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/
#SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-vz!lj^+vf@!(6&07mgt6r*u72%!g-2@tqa*3fqc_g1y=!$x(hk"


#SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ["*"]


#Application definition
INSTALLED_APPS = [
    "jazzmin",
    
    "django.contrib.admin",
    
    "django.contrib.auth",
    
    "django.contrib.contenttypes",
    
    "django.contrib.sessions",
    
    "django.contrib.messages",
    
    "django.contrib.staticfiles",
    
    "django.contrib.sites",
    
    "allauth",
    
    "allauth.socialaccount",
    
    "allauth.socialaccount.providers.google",
    
    "allauth.socialaccount.providers.facebook",
    
    "authentications",
    
    "reports",

    "managements",
    
    "auxiliaries"
]


SITE_ID = 1


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    
    "django.contrib.sessions.middleware.SessionMiddleware",
    
    "django.middleware.common.CommonMiddleware",
    
    "django.middleware.csrf.CsrfViewMiddleware",
    
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    
    "django.contrib.messages.middleware.MessageMiddleware",
    
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    
    "allauth.account.middleware.AccountMiddleware",
]


ROOT_URLCONF = "configurations.urls"


TEMPLATES = [
    {   
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        
        "DIRS": [os.path.join(BASE_DIR, "statics/templates/")],
        
        "APP_DIRS": True,
        
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                
                "django.template.context_processors.request",
                
                "django.contrib.auth.context_processors.auth",
                
                "django.contrib.messages.context_processors.messages",
                
                "authentications.processors.coordinates",
            ],
            
        },

    },

]


WSGI_APPLICATION = "configurations.wsgi.application"


#Database
#https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        
        "OPTIONS": {
            "options": "-c search_path=cotseye_schema"
        },

        "NAME": "cotseye",
        
        "USER": "postgres",
        
        "PASSWORD": "reydel",
        
        "HOST": "localhost",

        "PORT": "5433",
    }
}


#Password validation
#https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    #{
    #    "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    #},

    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },

    #{
    #    "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    #},

    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


#Internationalization
#https://docs.djangoproject.com/en/4.2/topics/i18n/
LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Manila"

USE_I18N = True

USE_TZ = True

DATETIME_FORMAT = "%b. %j, %Y %I:%M %P"


#Static files (CSS, JavaScript, Images)
#https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = "statics/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "statics")
]

MEDIA_URL = "assets/"

MEDIA_ROOT = os.path.join(BASE_DIR, "statics/assets")


#Default primary key field type
#https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


AUTH_USER_MODEL = "authentications.Account"

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

SOCIALACCOUNT_LOGIN_ON_GET = True

SOCIALACCOUNT_AUTO_SIGNUP = True

SOCIALACCOUNT_EMAIL_VERIFICATION = "none"

SOCIALACCOUNT_EMAIL_REQUIRED = False

SOCIALACCOUNT_QUERY_EMAIL = False

ACCOUNT_USER_MODEL_EMAIL_FIELD = None

ACCOUNT_EMAIL_REQUIRED = False

ACCOUNT_UNIQUE_EMAIL = False

ACCOUNT_EMAIL_VERIFICATION = "none"

ACCOUNT_AUTHENTICATION_METHOD = "username"

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            
            "email",
        ],

        "AUTH_PARAMS": {
            "access_type": "online",
        }
    },

    "facebook": {
        "SCOPE": [
            "public_profile",
            
            "email",
        ],

        "AUTH_PARAMS": {
            "access_type": "online",
        }
    },
}


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "smtp.gmail.com"

EMAIL_PORT = 587

EMAIL_USE_TLS = True

EMAIL_HOST_USER = "cotseye.information@gmail.com"

EMAIL_HOST_PASSWORD = "vqmurhtaaynudqku"


RECAPTCHA_PUBLIC_KEY = "6LfYwRMnAAAAAG8B0ZyMeD-NNV1pnVFlXS_A0-yV"

RECAPTCHA_PRIVATE_KEY = "6LfYwRMnAAAAAIHt-ewPrUDtpE3Uxwr5Xa6-tqL-"


JAZZMIN_SETTINGS = {
    "changeform_format": "horizontal_tabs",
        
    "custom_css": "css/officer/control/index/index.css",

    "custom_css": "css/admin/control/index/index.css", 

    "copyright": "Team Rocket",

    "navigation_expanded": False,

    "show_sidebar": False,

    "site_brand": "COTSEye",
    
    "site_logo": "assets/icons/logo.png",

    "topmenu_links": [
        {"name": "Access statistics", "url": reverse_lazy("admin:Administrator Control Statistics")}
    ]
}