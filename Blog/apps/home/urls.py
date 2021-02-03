from django.urls.conf import include, path
from . import views

urlpatterns = [
    path( '', views.RenderHome, name = "Home"),
    path('posts/<int:index>', views.RenderPost, name="render_post"),
]
