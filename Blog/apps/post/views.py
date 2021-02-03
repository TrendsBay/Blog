from django.shortcuts import redirect, render
from ..home.models import posts
# Create your views here.

## get the post in a specific index
def GetPost(index): # index is the index of our post in database
    return posts.objects.get(id=int(index))

def RenderPost(request, index = 1):
    post = GetPost(index);
    post_jason = {
        'site_name' : 'Blog',
        'post' : post,
    };
    return render(request, "show_post_template.html", post_jason);

def testpost(args):
    print("testing");
    
