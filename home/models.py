from django.db import models



class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)
    )


     def __str__(self):
        return self.name

        @classmethod
        def get_items_by_cuisine(cls, cuisine_type):
            """
            Return a QuerySet of menu items filltered by the given cuisine type.

            Args:
            cuisine_type (str): The cuisine tpye to filter by. 

            Returns:
              QuerySet: A filtered QuerySet of MenuItem objects.
              """
              return cls.objects.filter(cuisine__iexact=cuisine_type)