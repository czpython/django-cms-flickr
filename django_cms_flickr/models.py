from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from cms.models.pluginmodel import CMSPlugin

from apis.flickr.flickr import FlickrAPI

try:
    API_KEY = settings.FLICKR_API_KEY
    SECRET = settings.FLICKR_API_SECRET
except AttributeError:
    raise ImproperlyConfigured, u"Need to define FLICKR_API_KEY and FLICKR_SECRET"


class CMSFlickrGallery(CMSPlugin):
    # Here i add the model's name to the field due to a bug in django-cms
    # in which field names cause conflict
    cms_flickr_gallery_name = models.CharField(_("Gallery Name"), max_length=75, blank=True,
                                help_text="If not provided, then will use name from flickr", unique=True)
    cms_flickr_gallery_slug = models.SlugField(_("Slug for this gallery"), max_length=100, editable=False,
                                help_text="If not provided, then will use name field", unique=True)
    cms_flickr_gallery_set_id = models.BigIntegerField(_("Flickr photoset id"), max_length=100, unique=True)
    cms_flickr_gallery_per_page = models.SmallIntegerField(_("Photos to load per page"), max_length=3, default=30)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name:
            flickr = FlickrAPI(API_KEY, SECRET)
            photoset = flickr.get_photoset(photoset_id=self.set_id)
            self.name = photoset['title']
        self.slug = slugify(self.name)
        super(FlickrGallery, self).save(*args, **kwargs)
