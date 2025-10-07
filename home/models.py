from django.db import models


class MenuItem(models.Model):
     name = models.CharField(max_length=100)
     description = models.TextField(blank=True, null=True)
     price = models.FloatField()
     discount_percent = models.FloatField(default=0.0, help_text="Discount percentage on the item (0-100")

    
    def __str__(self):
        return self.name


    def get_final_price(self) -> float:
        """
        Calculate the final price after applying discount.
        Return a float rounded to 2 decimal places.
        """
        if self.discount_percent > 0:
            discount_amount = (self.price * self.discount_percent) / 100
            final_price = self.price - discount_amount
        else:
            final_price = self.price

            return round(final_price,2)


