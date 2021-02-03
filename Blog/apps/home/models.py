from django.db import models

# Create your models here.

## PRE MADE COMPUTER TABLE
class posts(models.Model):
    heading = models.CharField(max_length=300)
    small_description = models.CharField(max_length=256)
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to="static/images/")
    

    def __str__(self):
        return f"{self.pk} | {self.heading}"