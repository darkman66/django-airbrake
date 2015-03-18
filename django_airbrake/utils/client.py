import sys
import traceback
import airbrake
from django.conf import settings
from django.core.urlresolvers import resolve
from lxml import etree


class Client(object):
    DEFAULTS = {
        'TIMEOUT': 5,
        'USE_SSL': False,
    }

    @property
    def url(self):
        scheme = 'http'
        if self.settings['USE_SSL']:
            scheme = 'https'

        return Client.API_URL % scheme


    @property
    def settings(self):
        if getattr(self, '_settings', None):
            return self._settings

        self._settings = Client.DEFAULTS
        self._settings.update(getattr(settings, 'AIRBRAKE', {}))
        return self._settings


    def notify(self, exception=None, request=None):
        headers = {
            'Content-Type': 'text/xml'
        }
        try:
            air_log = airbrake.getLogger(api_key = self.settings.AIRBRAKE['API_KEY'],
                                        project_id = self.settings.AIRBRAKE['PROJECT_ID'],
                                         environment = self.settings.AIRBRAKE['ENVIRONMENT'])
            air_log.exception(str(exception))
        except Exception ,e:
            print 'Airbrake exception: %s\n\n%s' % (e, traceback.format_exc())

