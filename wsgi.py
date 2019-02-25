# wsgi.py
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "issue_tracker_0_2.settings.production")

application = get_wsgi_application()
