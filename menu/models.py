from django.db import models

class Category(models.Models):
      category_name = models.CharField(max_length=100)


      def __str__(self):
          return self.category_name

class MenuItem(models.Model):

    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)

     def __str__(self):
        return self.name