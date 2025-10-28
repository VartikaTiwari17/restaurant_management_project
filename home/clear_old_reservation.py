from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta
from home.models import Reservation  # Make sure your model name is correct

class Command(BaseCommand):
    help = 'Deletes old unconfirmed reservations older than 24 hours.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--hours',
            type=int,
            default=24,
            help='Specify how many hours old reservations should be before deletion.',
        )

    def handle(self, *args, **options):
        hours = options['hours']
        threshold_time = timezone.now() - timedelta(hours=hours)

        old_reservations = Reservation.objects.filter(
            status__in=['pending', 'unconfirmed'],
            created_at__lt=threshold_time
        )

        count = old_reservations.count()
        old_reservations.delete()

        self.stdout.write(
            self.style.SUCCESS(f'Successfully deleted {count} old unconfirmed reservations older than {hours} hours.')
        )
