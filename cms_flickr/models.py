from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin

FLICKR_TEMPLATES = settings.FLICKR_TEMPLATES


# Thanks to https://github.com/lazerscience/cmsplugin-flickr for these constants

ALL_TAGS = 'all'
ANY_TAG = 'any'
TAG_MODE_CHOICES = ((ANY_TAG, _('Any Tag')),
                    (ALL_TAGS, _('All Tags')))

DATE_POSTED_ASC = 'date-posted-asc'
DATE_POSTED_DESC = 'date-posted-desc'
DATE_TAKEN_ASC = 'date-taken-asc' 
DATE_TAKEN_DESC = 'date-taken-desc'
INTERESTINGNESS_ASC = 'interestingness-asc' 
INTERESTINGNESS_DESC = 'interestingness-desc'
RELEVANCE = 'relevance'

ORDER_CHOICES =((DATE_POSTED_ASC, _('Date Posted Ascending')),
                (DATE_POSTED_DESC, _('Date Posted Descending')),
                (DATE_TAKEN_ASC, _('Date Taken Ascending')),
                (DATE_TAKEN_DESC, _('Date Taken Descending')),
                (INTERESTINGNESS_ASC, _('Interestingness Ascending')),
                (INTERESTINGNESS_DESC, _('Interestingness Descending')),
                (RELEVANCE, _('Relevance')))

SMALL_SQUARE = 's'
THUMBNAIL = 't'
SMALL = 'm'
MEDIUM = '-'
LARGE = 'b'
ORIGINAL = 'o'

SIZE_CHOICES = ((SMALL_SQUARE, _('Small Square 75px x 75px')),
                (THUMBNAIL, _('Thumbnail, 100px on longest side')),       
                (SMALL, _('Small, 240px on longest side')),
                (MEDIUM, _('Medium, 500px on longest side')),
                (LARGE, _('Large, 1024px on longest side')),
                (ORIGINAL, _('Original image')))


class FlickrGalleryOrPhotoset(CMSPlugin):

    GALLERY = 'gallery'
    PHOTOSET = 'photoset'

    APIS = {GALLERY: 'galleries', PHOTOSET: 'photosets'}

    TYPES = (
        (GALLERY, 'Gallery'),
        (PHOTOSET, 'Photoset'),
    )

    flickr_api_type = models.CharField(_("Collection Type"), max_length='10', choices=TYPES, 
        help_text="Is this a Gallery or Photoset ?")
    flickr_fid = models.CharField(_("Flickr Gallery or Photoset Id"), max_length=75)
    flickr_photocount = models.IntegerField(_("How many photos ?"), default=500)
    flickr_photo_size = models.CharField(_("Photo size"), choices=SIZE_CHOICES, max_length=1, default=SMALL_SQUARE)
    flickr_template = models.CharField(_("Photo Layout Template"), choices=FLICKR_TEMPLATES, max_length=200, default=FLICKR_TEMPLATES[0][0])

    def __unicode__(self):
        return self.flickr_api_type
