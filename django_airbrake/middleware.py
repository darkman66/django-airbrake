from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed
from django_airbrake.utils.client import Client

class AirbrakeNotifierMiddleware(object):
    def __init__(self):
        print '1'*80
        self.client = Client()

    def process_exception(self, request, exception):
        print 'a'*80
        if hasattr(settings, 'AIRBRAKE') and not settings.AIRBRAKE.get('DISABLE', False):
            print '>'*80
            self.client.notify(exception=exception, request=request)
