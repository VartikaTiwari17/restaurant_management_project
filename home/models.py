from account import models


class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    # ✅ New field added
    description = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
