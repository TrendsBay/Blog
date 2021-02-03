from django.conf.urls import url
from django.urls.conf import include, path
from . import views
from ..home import views as home_views

urlpatterns = [
    path( "", views.RenderPost, name = "posts"),
    path( "posts/<int:index>?find=<str:data>", home_views.RenderHome),
]
