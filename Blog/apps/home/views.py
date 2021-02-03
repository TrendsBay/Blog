from django.http import request
from django.http.request import HttpRequest
from django.shortcuts import render
from .models import posts

# Create your views here.
def RenderHome(request):

    all_posts = posts.objects.all();
    home_json = {
        'site_name' : 'Blog',
        'posts' : all_posts,
    };
    return render(request, "show_posts_template.html", home_json)