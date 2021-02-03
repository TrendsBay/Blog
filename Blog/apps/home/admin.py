from django.contrib import admin
from .models import posts, UserProfile

# Register your models here.
# admin.site.unregister(posts)
admin.site.register(posts)
admin.site.register(UserProfile)