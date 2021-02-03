from django.urls.conf import include, path
from . import views

urlpatterns = [
    path( '', views.RenderHome, name = "Home"),
    path('post', include("apps.post.urls")),
]
