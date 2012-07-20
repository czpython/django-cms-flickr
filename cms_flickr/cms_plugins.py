import json

from django.conf import settings
from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cms_flickr.models import FlickrGalleryOrPhotoset

from flickrapi import FlickrAPI, FlickrError

API_KEY = settings.FLICKR_API_KEY

SECRET = settings.FLICKR_SECRET

FLICKR_TEMPLATES = settings.FLICKR_TEMPLATES

FLICKR_IMAGE_URL = "http://farm%(farm)s.static.flickr.com/%(server)s/%(id)s_%(secret)s_%(size)s.jpg"

class FlickrGalleryOrPhotosetPlugin(CMSPluginBase):
    model = FlickrGalleryOrPhotoset
    name = _("Flickr Gallery/Photoset")
    admin_preview = False
    render_template = FLICKR_TEMPLATES[0][0]

    def render(self, context, instance, placeholder):
        flickr = FlickrAPI(API_KEY, SECRET)

        call = '%s.%s' % (FlickrGalleryOrPhotoset.APIS[instance.flickr_api_type], 'getPhotos')
        api = getattr(flickr, call)
        
        type_id = instance.flickr_api_type + '_id'
        params = {type_id: instance.flickr_fid, 'per_page': instance.flickr_photocount, 
        'format': 'json', 'nojsoncallback':'1', 'extras': 'url_s, url_q, url_t,  url_m, url_n, url_-, url_z, url_b, url_o'}
        try:
            response = json.loads(api(**params))
        except FlickrError, e:
            error = "FlickrAPI Error: " + str(e)
            context.update({'flickr_error': error})
        photos = response['photoset'].get('photo')
        photo = photos[0]
        if photos:
            for photo in photos:
                photo['url'] = photo.get('url_%s' % instance.flickr_photo_size)
                photo['width'] = photo.get('width_%s' % instance.flickr_photo_size)
                photo['height'] = photo.get('height_%s' % instance.flickr_photo_size)

        self.render_template = instance.flickr_template
        context.update({
            'obj': instance,
            'photos': photos,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(FlickrGalleryOrPhotosetPlugin)
