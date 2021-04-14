import os
import uuid

from django.utils.translation import ugettext_lazy as _


DEBUG = False

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(PROJECT_DIR))

ROOT_URLCONF = 'page_transitions.urls'
WSGI_APPLICATION = 'page_transitions.wsgi.application'

SECRET_KEY = str(uuid.uuid4().hex)
ALLOWED_HOSTS = []

DEFAULT_FROM_EMAIL = SERVER_EMAIL = 'page_transitions@moccu.me'
EMAIL_SUBJECT_PREFIX = os.path.basename(PROJECT_DIR)

LANGUAGES = [
    ('de', _('German')),
]
LANGUAGE_CODE = 'de'
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_L10N = True
USE_TZ = True

USE_ETAGS = True

SITE_ID = 1

SESSION_COOKIE_SECURE = True
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'template_helpers',
    'inline_static',
    'static_templates',

    'page_transitions.accounts.apps.AccountsConfig',
    'page_transitions.core.apps.CoreConfig',
)

MIGRATION_MODULES = {
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(ROOT_DIR, 'templates')],
        'OPTIONS': {
            'debug': False,
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'template_helpers.context_processors.settings',
            ],
        },
    },
]

AUTH_USER_MODEL = 'accounts.User'

LOCALE_PATHS = (
    os.path.join(ROOT_DIR, 'templates/locale'),
)

MIDDLEWARE = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

MEDIA_ROOT = os.path.join(ROOT_DIR, 'web', 'media')
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(ROOT_DIR, 'web', 'static')
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
STATICFILES_DIRS = (
    os.path.join(ROOT_DIR, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_TEMPLATES = [
    ('500.html', 'errors/500.html'),
]

CACHE_MIDDLEWARE_SECONDS = 60

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '[{asctime}] {levelname} {message}',
            'style': '{',
        }
    },
    'handlers': {
        'null': {
            'class': 'logging.NullHandler',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'page_transitions': {
            'level': 'DEBUG',
            'handlers': ['console'],
        },
        'django': {
            'level': 'WARNING',
            'handlers': ['console'],
        },
        'django.server': {
            'level': 'INFO',
            'handlers': ['console'],
        },
    }
}

TEMPLATE_EXPOSED_SETTINGS = (
    'DEBUG',
)
