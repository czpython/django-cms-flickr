from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

try:
    FLICKR_TEMPLATES = settings.FLICKR_TEMPLATES
except AttributeError, e:
    raise ImproperlyConfigured('Please define FLICKR_TEMPLATES in your settings.py')

try:
    API_KEY = settings.FLICKR_API_KEY
    SECRET = settings.FLICKR_SECRET
except AttributeError:
    raise ImproperlyConfigured, u"Need to define FLICKR_API_KEY and FLICKR_SECRET"