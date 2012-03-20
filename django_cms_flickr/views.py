from django.shortcuts import render_to_response, get_object_or_404
from django.http import (
    HttpResponseRedirect,
    HttpResponse,
    Http404,
)
from django.core.exceptions import ImproperlyConfigured
from django.template import RequestContext
from django.conf import settings
from django.contrib import messages


try:
    API_KEY = settings.FLICKR_API_KEY
    SECRET = settings.FLICKR_API_SECRET
except AttributeError:
    raise ImproperlyConfigured, u"Need to define FLICKR_API_KEY and FLICKR_SECRET" 


def get_photos(request, slug, page=1, template="acf/photos.html", 
                    page_template="cms/flickr/loaded-photos.html"):

    """ Retrieves all the photos from photoset 'name' ."""

    try:
        gallery = FlickrGallery.objects.get(slug=slug)
    except FlickrGallery.DoesNotExist:
        raise Http404

    flickr = FlickrAPI(API_KEY, SECRET)
    photoset_id = gallery.set_id
    try:
        page = int(page)
    except TypeError:
        page = 1
    try:
        response = flickr.get_photoset_photos(photoset_id=gallery.set_id, 
                                                per_page=gallery.per_page, page=page) 
    except FlickrAPIError:
        raise Http404

    # Complex pagination :)
    next = page + 1
    if request.is_ajax():
        template = page_template
    photos = response['photo']
    pages = response['pages']
    del response
    return render_to_response(template, locals(), 
                                context_instance=RequestContext(request))


def get_photo(request, slug, photoid):
    try:
        gallery = FlickrGallery.objects.get(slug=slug)
    except FlickrGallery.DoesNotExit:
        raise Http404
    flickr = FlickrAPI(API_KEY, SECRET)
    try:
        photo = flickr.get_photo_info(photo_id=photoid)
        sizes = flickr.get_sizes(photo_id=photoid)
    except FlickrAPIError:
        raise Http404
    return render_to_response("cms/flickr/photo.html", {'photoset': slug, 'photo': photo, 'sizes': sizes}, 
                                context_instance=RequestContext(request))
