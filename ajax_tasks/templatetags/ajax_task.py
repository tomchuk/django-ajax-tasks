from django import template
from django.conf import settings
from django.core.urlresolvers import reverse
from django.core.cache import cache

import base64
import hashlib
import itertools
import json

register = template.Library()

class AjaxTaskNode(template.Node):
    def __init__(self, task_name, task_args):
        self.task_name = task_name
        self.task_args = [template.Variable(arg) for arg in task_args]
    def render(self, context):
        task_args = dict([(str(arg), arg.resolve(context)) for arg in self.task_args])
        cache_key = hashlib.md5(self.task_name + ''.join(task_args.values())).hexdigest()
        data = cache.get(cache_key)

        # support for multiple calls per page load
        if self not in context.render_context:
            context.render_context[self] = itertools.count()
        count = next(context.render_context[self])

        if data:
            t = template.loader.get_template('ajax_tasks/%s_display.html' % self.task_name)
            return t.render(template.Context({'data': data}, autoescape=context.autoescape))
        else:
            # NOTE: Base 64 encoding is done with url safe
            # 63rd param of '_' intead of the standard '/'
            args_str = base64.b64encode(json.dumps(task_args), '+_')
            url = reverse('ajax_tasks_dispatch', kwargs = {
                'task_name':self.task_name,
                'task_args':args_str })
            output = '''<div class="ajax-task" id="ajax-task-{count}"
                rel="{url}"></div>'''.format(count=count, url=url)
            if count == 0:
                output += '''
                    <script>window.jQuery || document.write('<script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.0/jquery.min.js"><\/script>');</script>
                    <script>
                        jQuery(function($){
                            $('.ajax-task').each(function(){
                                var _this = $(this);
                                $.get(_this.attr('rel'), function(data, textStatus, jqXHR){
                                    _this.replaceWith(data);
                                });
                            });
                        });
                    </script>

                '''
            return output

@register.tag
def ajax_task(parser, token):
    try:
        tokens = token.split_contents()
        tag_name = tokens.pop(0)
        task_name = tokens.pop(0)
        task_args = tokens
    except IndexError:
        raise template.TemplateSyntaxError('%r tag requires at least two arguments: task name as defined in the AJAX_TASKS variable in settings and at at least one argument' % token.contents.split()[0])
    return AjaxTaskNode(task_name, task_args)
