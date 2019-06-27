import subprocess
import sys
import signal
import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Install Deps Frontend'

    def handle(self, *args, **options):
        proc = None

        try:
            proc = subprocess.Popen(
                ['npm', 'install'], stdout=sys.stdout, stderr=sys.stderr, cwd='website/')
        except KeyboardInterrupt:
            os.kill(proc.pid, signal.SIGKILL)
