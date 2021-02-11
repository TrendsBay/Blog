from django.db import models
from ..accounts import models as accounts

## PRE MADE COMPUTER TABLE

class posts(models.Model):
    author = models.ForeignKey(accounts.UserProfile, on_delete=models.CASCADE);
    heading = models.CharField(max_length=300);
    small_description = models.CharField(max_length=256);
    body = models.TextField();
    image = models.ImageField(upload_to="static/images/");
    
    def __str__(self):
        return f"{self.pk} | {self.heading}"

    def get_posts():
        return posts.objects.all().order_by('id').reverse();