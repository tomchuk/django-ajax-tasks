from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'dispatch/(?P<task_name>[-_a-zA-z]+)/(?P<task_args>[_+A-Za-z0-9=]+)/$',
        'ajax_tasks.views.dispatch', name='ajax_tasks_dispatch'),
)
