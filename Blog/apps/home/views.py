from django.http import request
from django.http.request import HttpRequest
from django.shortcuts import render
from .models import posts

def RenderHome(request):
    
    # getting the search value if there is no search data we will initialise data = None
    data = request.GET.get("find", None);

    if data == None:
        _posts = posts.get_posts();
    else:
        _posts = posts.objects.all().filter(heading__contains=str(data))

    home_json = {
        'site_name' : 'Blog',
        'posts' : _posts,
        'post_count' : _posts.count(),
    };
    
    return render(request, "show_posts_template.html", home_json);


## get the post in a specific index
def GetPost(index): # index is the index of our post in database
    return posts.objects.get(id=int(index))

def RenderPost(request, index = 1):

    data = request.GET.get("find", None);
    if data == None: 
        post = GetPost(index);
    else :
        return RenderHome(request);

    post_jason = {
        'site_name' : 'Blog',
        'post' : post,
    };
    return render(request, "show_post_template.html", post_jason);