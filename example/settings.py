import os.path
DEBUG = TEMPLATE_DEBUG = True
SECRET_KEY='123'
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'example'
    }
}
ROOT_URLCONF = 'urls'
WSGI_APPLICATION = 'wsgi.application'
TEMPLATE_DIRS = (os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates')),)
INSTALLED_APPS = (
    'ajax_tasks',
    'flickr',
)

FLICKR_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

AJAX_TASKS = {
    'flickr': ('flickr.views.flickr_task', 60),
}
