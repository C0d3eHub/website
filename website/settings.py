"""
Django settings for your project.
"""

import os
from pathlib import Path
from decouple import config 
from dotenv import load_dotenv
load_dotenv()


# Required for Django CMS v4 compatibility
CMS_CONFIRM_VERSION4 = True

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-secret-key')  # Store in environment variables for security

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'  # Set to False in production
#cookies
# settings.py
SESSION_COOKIE_AGE = 600  # 10 minutes in seconds

# Allowed hosts
ALLOWED_HOSTS = ['shekhar36.pythonanywhere.com', 'localhost', '127.0.0.1','itikuthar.pythonanywhere.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
    'django.contrib.sites',  # Ensure this is included for django-cms
    'cms',  # Django CMS app
    'menus',  # Required for Django CMS
    'treebeard',  # Required for Django CMS
    'main_app',  # Your custom app
    #'jet',  # django-jet for enhanced admin interface
]

MIDDLEWARE = [

    
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'main_app', 'templates')],  # Point to your custom templates directory
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

WSGI_APPLICATION = 'website.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'OPTIONS': {
            'timeout': 20,  # Increase timeout to 20 seconds
        },
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'main_app', 'static')]  # Add your static directory
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # For production use

# Media files (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Add this line to define the current site (usually '1' for a single site setup)
SITE_ID = 1

# Enable the CMS
CMS_TEMPLATES = [
    ('template.html', 'Template Name'),  # Replace with your actual template file name
]

# CSRF settings (optional for HTTPS)
CSRF_COOKIE_SECURE = not DEBUG  # Set to True in production
SESSION_COOKIE_SECURE = not DEBUG  # Set to True in production



# Logging configuration (optional)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'ERROR',  # Change to 'ERROR' or 'WARNING' in production
        },
    },
}

# Caching settings (optional)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

# Email settings (for Gmail SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'your_email@gmail.com')  # Set this via environment variables
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')  # Store this securely in environment variables
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER  # Default email sender

# Console email backend for local testing (optional)
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


