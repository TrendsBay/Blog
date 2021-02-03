from django.urls.conf import include, path
from . import views

urlpatterns = [
    path( '', views.RenderHome, name = "Home"),
    path('posts/<int:index>', include("apps.post.urls")),
]
