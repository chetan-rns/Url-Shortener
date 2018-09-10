from django.core.management.base import BaseCommand, CommandError
from shortener.models import *

class Command(BaseCommand):
    help = 'Refreshes all url shortcodes'

    

    def handle(self, *args, **options):
        return urlData.objects.refresh_shortcodes()