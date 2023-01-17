from django.shortcuts import render,HttpResponseRedirect
from datetime import date
from .models import Post
from .form import PostForm
from django.views import View
from django.views.generic import ListView,DetailView
#all_posts = Post.objects.all()



def index(request):
    latest_posts = Post.objects.all().order_by("-date")
    return render(request,"myblog/index.html",{
        "posts": latest_posts
    })

def post_details(request,slug):
    identified_posts = Post.objects.get(slug = slug)
    return render(request, "myblog/post_details.html",{
        "post": identified_posts
    })

def thank_you(request):
    return render(request, "myblog/thank-you.html")


class PostDetails(DetailView):
    model = Post
    template_name= "myblog/post_details.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post"] = Post.objects.get(slug = kwargs['object'].slug)
        return context
     

class GetPosts (View):
    def get(self,request):
        form = PostForm()
        return render(request, "myblog/post_form.html",{
        "form": form
    })

    def post(self,request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("thank-you")
        return render(request, "myblog/post_form.html",{
        "form": form
    })

class Posts(ListView):
    model = Post
    template_name="myblog/all_posts.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sorted_posts = Post.objects.all().order_by("-date")
        context["posts"] = sorted_posts
        return context

# def index(request):
#     latest_posts = Post.objects.all().order_by("-date")
#     return render(request,"myblog/index.html",{
#         "posts": latest_posts
#     })

class MainIndex(ListView):
    model = Post
    template_name = "myblog/index.html"
    def get_queryset(self):
        base_query=super().get_queryset()
        return base_query.order_by("-date")
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(pk__gte=3)
        return context
    

    

    
