import csv
from django.core.management.base import BaseCommand
from home.models import MenuItem, MenuCategory

class Command(BaseCommand):
    help = "Import menu items from a CSV file and create/update MenuCategory and MenuItem objects."

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file containing menu items')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        try:
            with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    category_name = row.get('category_name')
                    category, _ = MenuCategory.objects.get_or_create(name=category_name)

                    MenuItem.objects.update_or_create(
                        name=row['name'],
                        defaults={
                            'description': row.get('description', ''),
                            'price': row.get('price', 0.00),
                            'category': category
                        }
                    )
                self.stdout.write(self.style.SUCCESS("✅ Menu items imported successfully!"))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"❌ File not found: {csv_file_path}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"⚠️ Error importing menu items: {str(e)}"))
