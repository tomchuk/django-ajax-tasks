from setuptools import setup

setup(
    name='django-ajax-tasks',
    version='0.1',
    description='A simple template tag to abstract the loading and caching of remote resources',
    long_description=open('README.md').read(),
    author='Thomas Achtemichuk',
    author_email='tom@tomchuk.com',
    url='https://github.com/tomchuk/django-ajax-tasks',
    download_url='https://github.com/tomchuk/django-ajax-tasks/downloads',
    license='BSD',
    packages=['ajax_tasks',],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
