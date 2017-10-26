""" WSGI configuration
:Author: Jonathan Karr <karr@mssm.edu>
:Date: 2017-10-25
:Copyright: 2017, Karr Lab
:License: MIT
"""

import sys, os

# Use custom version of python
INTERP = "/home/minicell/opt/python-3.6.3/bin/python3"
if os.path.isfile(INTERP) and sys.executable != INTERP:	
    os.execl(INTERP, INTERP, *sys.argv)    

# Instantiate application
from django.core.wsgi import get_wsgi_application
os.environ["DJANGO_SETTINGS_MODULE"] = "minicell.site.settings"
application = get_wsgi_application()
