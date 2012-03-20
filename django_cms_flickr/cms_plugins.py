from django.conf import settings
from django.utils.translation import ugettext as _
from django.core.exceptions import ImproperlyConfigured

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django_cms_flickr.models import CMSFlickrGallery

try:
    API_KEY = settings.FLICKR_API_KEY
    SECRET = settings.FLICKR_API_SECRET
except AttributeError:
    raise ImproperlyConfigured, u"Need to define FLICKR_API_KEY and FLICKR_SECRET"


class FlickrGalleryPlugin(CMSPluginBase):
    model = CMSFlickrGallery
    name = _("Gallery")
    admin_preview = False
    render_template = "cms/flickr/photoset.html"

    def render(self, context, instance, placeholder):
        flickr = FlickrAPI(API_KEY, SECRET)
        photoset = flickr.get_photoset(photoset_id=instance.gallery.set_id)
        context.update({
            'obj': instance,
            'photoset': photoset,
            'placeholder': placeholder
        })
        return context
