from django.db import models

# ✅ New model for dietary categories
class DietaryTag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# ⚙️ Assuming MenuItem model already exists:
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # ✅ Add Many-to-Many field for dietary tags
    dietary_tags = models.ManyToManyField(DietaryTag, blank=True, related_name='menu_items')

    def __str__(self):
        return self.name
