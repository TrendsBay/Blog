from django import urls
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('', include("apps.posts.urls")),
    path('accounts/', include('apps.accounts.urls')),
    path('admin/', admin.site.urls),
]
