from django.conf import settings
from django.core.cache import cache
from django.core.urlresolvers import get_callable
from django.shortcuts import render_to_response

import base64
import hashlib
import json

def dispatch(request, task_name=None, task_args=None):
    template_name = 'ajax_tasks/%s_display.html' % (task_name)
    # NOTE: Base 64 decoding is done with url safe
    # 63rd param of '_' intead of the standard '/'
    callable_args = json.loads(base64.b64decode(str(task_args), '+_'))
    template_data_fn = get_callable(settings.AJAX_TASKS[task_name][0])
    template_data = template_data_fn(**callable_args)
    cache_key = hashlib.md5(task_name + ''.join(callable_args.values())).hexdigest()
    cache.set(cache_key, template_data, settings.AJAX_TASKS[task_name][1])
    return render_to_response(template_name, {'data': template_data})

