# Django CMS Flickr

* Still under construction *

This is a Django CMS plugin for flickr sets/galleries.

It allows the user to integrate a flikr set on a page with minimal effort.
And provides useful tools such as dynamic loading ( endless scroller ).

 The plugin requires "Beej's `Python Flickr API`, get it from pypi.
 * Add it to your ``INSTALLED_APPS``::

```python
    INSTALLED_APPS = (
    	'....', 
    	'django_cms_flickr',
    )
```
 * Run ``python manage.py syncdb``
 * Obtain a Flickr API key at Flickr_.
 * Add the key and the secret to your ``settings.py``::

```python
    FLICKR_API_KEY = 'xxxx'
    FLICKR_API_SECRET = 'xxxx'
```

 * Place it on a page and use it!


.. _django CMS: http://www.django-cms.org
.. _Python Flickr API: http://stuvel.eu/projects/flickrapi
.. _Flickr: http://www.flickr.com/services/apps/create/apply

# Contribute

If you like the project, please, contact me at commonzenpython@gmail.com (gtalk and email) and help me improve it.