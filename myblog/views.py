from django.shortcuts import render,HttpResponseRedirect
from datetime import date
from .models import Post
from .form import PostForm

#all_posts = Post.objects.all()



def index(request):
    latest_posts = Post.objects.all().order_by("-date")
    return render(request,"myblog/index.html",{
        "posts": latest_posts
    })

def posts(request):
    sorted_posts = Post.objects.all().order_by("-date")
    return render(request,"myblog/all_posts.html",{
        "posts": sorted_posts
    })

def post_details(request,slug):
    # identified_posts = next(post for post in all_posts if post['slug'] == slug )
    identified_posts = Post.objects.get(slug = slug)
    return render(request, "myblog/post_details.html",{
        "post": identified_posts
    })

def thank_you(request):
    return render(request, "myblog/thank-you.html")

def get_posts(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("thank-you")
    else:
        form = PostForm()
    return render(request, "myblog/post_form.html",{
        "form": form
    })
    
    