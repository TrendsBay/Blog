from django.urls.conf import path
from . import views

urlpatterns = [
    path( "", views.RenderPost, name = "post"),
]
