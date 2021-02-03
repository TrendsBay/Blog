from django.shortcuts import render
from ..home.models import posts
# Create your views here.

## get the post in a specific index
def GetPost(index : int): # index is the index of our post in database
    return posts.objects.filter(id=index);
    for post in posts.objects.all():
        print(index, int(post.id))
        if int(post.id) is index:
            print("matched");
            return post;

    return 0;

def RenderPost(request):
    post = request.POST.get("post", None);
    # post = GetPost(id);
    post_jason = {
        'site_name' : 'Blog',
        'post' : post,
    };
    return render(request, "show_post_template.html", post_jason);
