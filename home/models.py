from django.db import models

# Define dietary choices at the top of the file
DIETARY_CHOICES = [
    ('VEGAN', 'Vegan'),
    ('VEGETARIAN', 'Vegetarian'),
    ('GLUTEN_FREE', 'Gluten-Free'),
    ('HALAL', 'Halal'),
    ('NONE', 'None'),
]

class MenuCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Allergen(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, related_name='menu_items')
    allergens = models.ManyToManyField(Allergen, blank=True)
    
    # 👇 New field added here
    dietary_preference = models.CharField(
        max_length=20,
        choices=DIETARY_CHOICES,
        default='NONE',
        blank=True,
        null=True,
        help_text="Select the dietary preference of this menu item (if any)."
    )

    def __str__(self):
        return self.name
