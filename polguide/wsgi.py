"""
WSGI config for polguide project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

if os.environ.get('DJANGO_DEVELOPMENT') is not None:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "polguide.settings.dev")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "polguide.settings.prod")

application = get_wsgi_application()
