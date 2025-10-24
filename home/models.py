from django.db import models



class Cuisine(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
        return self.name

    