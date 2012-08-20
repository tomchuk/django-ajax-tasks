from django.conf import settings
from django.shortcuts import render_to_response
import json
import urllib, urllib2

def home(request):
    query = request.GET.get('query', '')
    return render_to_response('home.html', {'query': query})

def flickr_task(query):
    flickr_url = 'http://api.flickr.com/services/rest/?'
    flickr_args = {
        'api_key': settings.FLICKR_KEY,
        'method': 'flickr.photos.search',
        'format': 'json',
        'nojsoncallback': 1,
        'sort': 'interestingness-desc',
        'per_page': 20,
        'text': query
    }
    result = json.loads(urllib2.urlopen(flickr_url + urllib.urlencode(flickr_args)).read())
    data = []
    for r in result['photos']['photo']:
        data.append({
            'link': 'http://www.flickr.com/photos/%s/%s' % (r['owner'], r['id']),
            'src': 'http://farm%s.staticflickr.com/%s/%s_%s_q.jpg' % (r['farm'], r['server'], r['id'], r['secret']),
            'title': r['title']
        })

    return data

