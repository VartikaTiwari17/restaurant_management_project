from django.db import models




class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_numbar = models. CharField(max_length=20)
    operating_days = models.CharField(
        max_length=100, 
        help_text="Enter days like: Mon, Tue, Wed, Thu, Fri,Sat,Sun "
        )

    def __str__(self):
          return self.name
