from django.db import models

# Create your models here.

# makemigrations - create changes and store in a file
# migrate - apply the pending changes created by migrations



class contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    message = models.TextField()


    def __str__(self):
        return self.name
    