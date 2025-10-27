class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def get_full_address(self):
        """
        Returns the restaurant's complete address as a single formatted string.
        """
        return f"{self.street_address}, {self.city}, {self.state} {self.zip_code}"

    def __str__(self):
        return self.name
