# django-airbrake



Django module for http://airbrake.io ...which works:)

I tried to use http://airbrake.io with one of my django projects. I found some modules around but all of them couldn't work with the latest airbrake API v3 so I decided to use on of existing modules and adjust it to my needs and make it work ...finally :)

This module works as django middelware. Tested with Django 1.4+

# set it up

First what you hae to do is to install python module for airbrake

    $ pip install -U airbrake

or go and get it form github from here

https://github.com/airbrake/airbrake-python

Next install django-airbrake module as follows

    $ git clone https://github.com/darkman66/django-airbrake.git
    $ cd django-airbrake
    $ python setup.py install
    
# Usage

For Django settings file of your prroject you have to add below lines anywhere BEFORE middleware classes section

    AIRBRAKE = {
      'API_KEY': '[your airbrake token]',
      'ENVIRONMENT': "[envirotment name]",
      'DISABLE' : False,
      'PROJECT_ID' : "[you project ID]"
    }
    
Now set up middleware

    MIDDLEWARE_CLASSES = (
      'django_airbrake.middleware.AirbrakeNotifierMiddleware',
      'django.middleware.gzip.GZipMiddleware',
      ...
    }
    
    
    
