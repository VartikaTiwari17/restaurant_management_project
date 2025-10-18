from django.db import models



class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('APPETIZER', 'Appetizer'),
        ('MAIN_COURSE', 'Main_Course'),
        ('DESSERT', 'Dessert'),
        ('BEVERAGE', 'Beverage'),
    ]


    name = models.CharField(max_length=100)
    Description  = models.TextField()
    price  = models. DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    category = models.ForeignKey('MenuCategory', on_delete=models.CASCADE)
    allergens = models.CharField(max_length=255, blank=True, null=True)
    )


     def __str__(self):
        if self.allergens:
            return f"{self.name}  (Allergens:  {self.allergens})"
        return self.name

    