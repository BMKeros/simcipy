import subprocess
import sys
import signal
import os
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Compile fronted Vue'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        proc = None

        try:
            proc = subprocess.Popen(
                ['npm', 'run', 'build'], stdout=sys.stdout, stderr=sys.stderr, cwd='website/')
        except KeyboardInterrupt:
            os.kill(proc.pid, signal.SIGKILL)
