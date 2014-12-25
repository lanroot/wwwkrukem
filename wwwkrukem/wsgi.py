"""
WSGI config for wwwkrukem project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "wwwkrukem.settings")
sys.path.append('/vhost/django-cms-installer.0.6.0-django-blog-zinnia-0.14.3/source/env/lib/python2.7/site-packages')
sys.path.append('/vhost/django-cms-installer.0.6.0-django-blog-zinnia-0.14.3/source')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
