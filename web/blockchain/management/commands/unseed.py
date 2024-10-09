from django.core.management.base import BaseCommand
from blockchain.models import EventData


class Command(BaseCommand):
    help = "Retrieve Contract Events"

    def handle(self, *args, **options):
        print("deleting all event data...")
        EventData.objects.all().delete()
