from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE);
    description = models.TextField();
    profile_pic = models.ImageField(upload_to="static/user_pictures/");

    def __str__(self):
        # for _user in self.user.objects.all():
        if (self.user.is_active):
                return f"{self.user.username}";
        else:
            return None;

    def get_all_users():
        return UserProfile.objects.all();

    def register(email,username,password):
        user = User.objects.create(username=username,email=email,password=password);
        user.save();

        profile = UserProfile.objects.create(user=user)
        profile.save();
