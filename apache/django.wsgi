import os, site, sys

path = '/Users/brab/Sites'
if path not in sys.path:
    sys.path.append(path)

site.addsitedir('/Users/brab/.virtualenvs/git_updater/lib/python2.7/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'git_updater.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

