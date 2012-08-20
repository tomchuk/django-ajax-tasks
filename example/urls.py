from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'flickr.views.home', name='home'),
    url(r'^ajax-tasks/', include('ajax_tasks.urls'))

)
