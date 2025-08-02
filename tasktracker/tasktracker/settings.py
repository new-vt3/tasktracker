# from pathlib import Path
# import os

# BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = 'your-secure-secret-key'
# DEBUG = True

# ALLOWED_HOSTS = ['*']  # Use specific domains in production

# SHARED_APPS = (
#     'django_tenants',
#     'customers', 
#     'django.contrib.contenttypes',
#     'django.contrib.staticfiles',
#     'tailwind',
#     # Add additional shared apps here
# )

# TENANT_APPS = (
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'tracker',              # Make sure this exists!
# )

# INSTALLED_APPS = list(SHARED_APPS) + [a for a in TENANT_APPS if a not in SHARED_APPS]

# TENANT_MODEL = "customers.Client"         # app.Model
# TENANT_DOMAIN_MODEL = "customers.Domain"  # app.Model

# MIDDLEWARE = [
#     'django_tenants.middleware.main.TenantMainMiddleware',  # must be first
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'tasktracker.urls'
# # PUBLIC_SCHEMA_URLCONF = 'tasktracker.urls_public'  # Uncomment if using

# WSGI_APPLICATION = 'tasktracker.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django_tenants.postgresql_backend',
#         'NAME': 'tasktracker',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# DATABASE_ROUTERS = (
#     'django_tenants.routers.TenantSyncRouter',
# )
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'arjavbadjate1404@gmail.com'
# EMAIL_HOST_PASSWORD = 'tvqy nozn ydvt yxrc'  # Not your Gmail password

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
# LOGIN_URL = '/login/'
# LOGIN_REDIRECT_URL = '/'
# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


from pathlib import Path
import os
import dj_database_url
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'unsafe-secret-key')
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

# Comma-separated ALLOWED_HOSTS in .env: "localhost,127.0.0.1,.yourdomain.com"
ALLOWED_HOSTS = [h.strip() for h in os.environ.get('ALLOWED_HOSTS', '*').split(',')]

# django-tenants configuration
SHARED_APPS = (
    'django_tenants',
    'customers',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'tailwind',
    # ... add other shared apps if any
)
TENANT_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'tracker',
    # ... add other tenant-specific apps if any
)
INSTALLED_APPS = list(SHARED_APPS) + [a for a in TENANT_APPS if a not in SHARED_APPS]

TENANT_MODEL = "customers.Client"
TENANT_DOMAIN_MODEL = "customers.Domain"

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',  # must come first!
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tasktracker.urls'
WSGI_APPLICATION = 'tasktracker.wsgi.application'
# # If you want a separate urlconf for the public schema, uncomment below:
# PUBLIC_SCHEMA_URLCONF = "tasktracker.urls_public"

# DATABASES - uses Render's DATABASE_URL
DATABASES = {
    'default': dj_database_url.parse(
        os.environ.get('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}
DATABASES['default']['ENGINE'] = 'django_tenants.postgresql_backend'

DATABASE_ROUTERS = ('django_tenants.routers.TenantSyncRouter',)

# Email config via .env (for Gmail/app password, etc.)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True').lower() == 'true'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Auth settings
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Tailwind
TAILWIND_APP_NAME = 'theme'
# NPM_BIN_PATH can be set if you have a custom npm location (mainly on Windows)
NPM_BIN_PATH = os.environ.get('NPM_BIN_PATH', 'npm') 

# TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # project-level templates
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

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
