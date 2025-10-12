from django.db import models


class MenuItem(models.Model):
     name = models.CharField(max_length=100)
     location = models.CharField(max_length=200, blank=True, null=True)

    
    def __str__(self):
        return self.name


    class OpeningHour(models.Model):
        Days_OF_WEEK = [Monday Tuesday wednesday thursday friday saturday sunday
            
        ]
        if self.discount_percent > 0:
            discount_amount = (self.price * self.discount_percent) / 100
            final_price = self.price - discount_amount
        else:
            final_price = self.price

            return round(final_price,2)


