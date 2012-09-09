import os, subprocess

from django.conf import settings
from django.views.generic.simple import direct_to_template

def update(request, site):
    site_path = settings.SITE_DIRS.get(site, '')
    if not site_path:
        return direct_to_template(request, '400.html', {
            'message': 'Site not found: %s' % site,
            })

    # Run the project's pull.sh script that handles updating the code
    # and running all necessary migrations
    subprocess.check_call(
            args='./pull.sh',
            cwd=site_path,
            shell=True,
            executable='/bin/bash')

    # Touch the wsgi file to restart the process
    try:
        os.utime(site_path + '/apache/django.wsgi', None)
    except:
        pass

    return direct_to_template(request, 'update.html', {
        'site': site,
        })
