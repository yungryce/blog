import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')

application = get_wsgi_application()


#import os
#import sys

#path = os.path.expanduser('~/setup')
#if path not in sys.path:
#    sys.path.insert(0, path)
#os.environ['DJANGO_SETTINGS_MODULE'] = 'setup.settings'
#from django.setup.wsgi import get_wsgi_application
#from django.contrib.staticfiles.handlers import StaticFilesHandler
#application = StaticFilesHandler(get_wsgi_application())
