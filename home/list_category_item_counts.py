from django.core.management.base import BaseCommand
from home.models import MenuCategory, MenuItem

class Command(BaseCommand):
    help = "Lists all menu categories along with the number of menu items in each."

    def handle(self, *args, **options):
        categories = MenuCategory.objects.all()
        if not categories.exists():
            self.stdout.write(self.style.WARNING("No menu categories found."))
            return

        for category in categories:
            item_count = MenuItem.objects.filter(category=category).count()
            self.stdout.write(f"{category.name}: {item_count} items")

        self.stdout.write(self.style.SUCCESS("Category item count listing complete."))
