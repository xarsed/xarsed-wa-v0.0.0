import os, django
from django.core import management
from django.contrib.sessions.management.commands import clearsessions


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xarsed_wa.settings')
django.setup()

cmd = clearsessions.Command()
management.call_command(cmd)