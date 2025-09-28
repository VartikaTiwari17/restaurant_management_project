from django.db import models



class ContactFromSubmission(models.Model):
     name = models.CharField(max_length=255)
     email = models.EmailField()
     message = models.TextField()
     submitted_at = models.DataTimeField(auto_now_add=True)



     def __str__(self):
        return f"{self.name} - {self.email}"