from django.db import models
from django.contrib.auth.models import User

# Create your models here.

## PRE MADE COMPUTER TABLE
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE);
    description = models.TextField();
    profile_pic = models.ImageField(upload_to="static/user_pictures/");

    def __str__(self):
        return f"{self.pk} | {self.user.username}"

class posts(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE);
    heading = models.CharField(max_length=300);
    small_description = models.CharField(max_length=256);
    body = models.TextField();
    image = models.ImageField(upload_to="static/images/");
    
    def __str__(self):
        return f"{self.pk} | {self.heading}"

    def get_posts():
        return posts.objects.all().order_by('id').reverse();