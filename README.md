django-ajax-tasks
=================

A simple template tag to abstract the loading and caching of remote resources

Motivation
==========

Many modern web applications rely on resources from external APIs and services. Whether that be a twitter stream, photos from Flickr, or other remote, high-latency data source. The current practice of loading these via AJAX works well at the expense of user experience due to rendering slowdowns and increased complexity of front-end code. `ajax_tasks` solves these two problems by caching and serving cached remote resources and automatically takes care of the front end JavaScript to load these resources asynchronously. It provides for the use of standard Django templates for displaying this data, a much cleaner and more designer-friendly solution that manipulating the DOM from JavaScript.

Installation
============

1. Set up `CACHES` in your settings.py.
2. Add `ajax_tasks` to your installed apps.
3. Include `ajax_tasks.urls` in your project urlpatterns. eg: `url(r'^ajax-tasks/', include('ajax_tasks.urls'))`
4. Add one or more tasks to the `AJAX_TASKS` variable `settings.py`. `AJAX_TASKS` is a dictionary which maps task names to a two tuple of a task function and a cache timeout. For example:

```python
AJAX_TASKS = {
        'flickr': ('flickr.views.flickr_task', 60),
        'twitter': ('foo.views.twitter_task', 360),
}
```

5. Write your task function. It should take one argument, that will be supplied via the template tag.
6. Write your task template. It should be located in the ajax_tasks subdirectory of your templates directory and be named `<task_name>_display.html`
7. Load the ajax_task template tag in the template you'd like to use it: `{% load ajax_task %}`
8. Call the template tag from your template with the task name and argument: `{% ajax_task <task_name> <task_arg> %}`

The `ajax_task` template tag will then check the cache for stored data. If present it will render the `<task_name>_display.html` template and insert it into the page. If the data is not cached, it will insert JavaScript that will make an ajax call to `ajax_tasks.views.dispatch` which will run the task, cache the results and return the rendered template to be inserted on the page.

Example App
===========

The provided example project should run out-of-the-box provided you fill in your Flickr API key in settings.py.
