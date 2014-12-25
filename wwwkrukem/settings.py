# -*- coding: utf-8 -*-
import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for wwwkrukem project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#03t!wc!$hm604^op!9oofv_o8o&ljeq!oy8qdfl03k-q5pi-&'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = False

TEMPLATE_DEBUG = True

#ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['parasite.kru.kem', 'cheese.kmr.ru']


# Application definition





ROOT_URLCONF = 'wwwkrukem.urls'

WSGI_APPLICATION = 'wwwkrukem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Krasnoyarsk'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'wwwkrukem', 'static'),
    ('assets', (os.path.join(BASE_DIR, 'wwwkrukem', 'static'))),
)
SITE_ID = 1

TEMPLATE_LOADERS = (
    'app_namespace.Loader',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings',
    'zinnia.context_processors.version',    # Optional
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'wwwkrukem', 'templates'),
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django_comments',
    'cms',
    'mptt',
    'menus',
    'sekizai',
    'whoosh',
    'haystack',
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'south',
    'reversion',
    'tagging',
#    'zinnia_threaded_comments',
    'zinnia_bootstrap',
    'zinnia',
    'zinnia_wymeditor',
    'cmsplugin_zinnia',
    'cmsplugin_wunderground',
    'cmsplugin_poll',
    'wwwkrukem',
    'userdir',
    'compressor',
    'debug_toolbar',
)

LANGUAGES = (
    ## Customize this
    ('ru', gettext('ru')),
)

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'ru',
            'hide_untranslated': False,
            'name': gettext('ru'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (
    ## Customize this
    ('page.html', 'Page'),
    ('feature.html', 'Page with Feature')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

DATABASES = {
    'default':
        {'ENGINE': 'django.db.backends.mysql', 'NAME': u'django_cms-2014-Dec-09', 'HOST': u'localhost', 'USER': '', 'PASSWORD': '', 'PORT': ''}
}


# debug_toolbar
# https://djangosnippets.org/snippets/1380/
from fnmatch import fnmatch
class glob_list(list):
    def __contains__(self, key):
        for elt in self:
            if fnmatch(key, elt): return True
        return False

INTERNAL_IPS = glob_list([
#    '127.0.0.1',
    '10.2.0.9',
    '10.2.0.143',
    '95.181.93.107'
    ])

#if DEBUG:
#    INSTALLED_APPS += ( 'debug_toolbar',)
#    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
DEBUG_TOOLBAR_PATCH_SETTINGS = False
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
SHOW_TOOLBAR_CALLBACK = True

#
# LOGGING
###
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
#            'filename': 'logs/mylog.log',
            'filename': os.path.join(BASE_DIR, 'logs/mylog.log'),
            'maxBytes': 1024*1024*5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
#            'filename': 'logs/django_request.log',
            'filename': os.path.join(BASE_DIR, 'logs/django_request.log'),
            'maxBytes': 1024*1024*5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {

        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}


#
# CMSPLUGIN-ZINNIA
###
#ZINNIA_ENTRY_BASE_MODEL = 'cmsplugin_zinnia.placeholder.EntryPlaceholder'

CMSPLUGIN_ZINNIA_APP_URLS = ['zinnia.urls']
# Default menu items for ZinniaApphook
#CMSPLUGIN_ZINNIA_APP_MENUS = (
#    'cmsplugin_zinnia.menu.EntryMenu',
#    'cmsplugin_zinnia.menu.CategoryMenu',
#    'cmsplugin_zinnia.menu.TagMenu',
#    'cmsplugin_zinnia.menu.AuthorMenu'
#)
# Non-default, No Sub-menus, Only 'Blog' menu item.
CMSPLUGIN_ZINNIA_APP_MENUS = ()

###default
CMSPLUGIN_ZINNIA_HIDE_ENTRY_MENU = True
### non-default, display yearly Blog Entry (for example: '2014')
#CMSPLUGIN_ZINNIA_HIDE_ENTRY_MENU = False
#
#CMSPLUGIN_ZINNIA_TEMPLATES = []


#
# django-cms-wunderground
###
WUNDERGROUND_KEY = '55110001241d540f'

#
# zinnia-threaded-comments
###
#COMMENTS_APP = 'zinnia_threaded_comments'

#
# Whoosh & django-haystack
###
WHOOSH_INDEX = os.path.join(BASE_DIR, 'whoosh/')

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': WHOOSH_INDEX,
    },
}

#HAYSTACK_SEARCH_ENGINE = 'whoosh'
#HAYSTACK_SITECONF = 'cmsplugin_search.search_sites'
#HAYSTACK_ITERATOR_LOAD_PER_QUERY = 10


#
# Django Compressor
# 1st & 2nd - it's a default finders for django
###
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# Default:	the opposite of DEBUG
# Boolean that decides if compression will happen. To test compression
# when DEBUG is True COMPRESS_ENABLED must also be set to True.
COMPRESS_ENABLED = True

#
# Caching & memcached
###
#CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
CACHE_MIDDLEWARE_SECONDS = 300
CACHE_MIDDLEWARE_KEY_PREFIX = 'wwwkrukem'
#CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
