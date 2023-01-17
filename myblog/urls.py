from django.urls import path
from . import views

urlpatterns = [
   # path("",views.index, name="main_page"),
    # path("posts", views.posts, name="posts_page"),
    path("",views.MainIndex.as_view(), name="main_page"),
    path("posts", views.Posts.as_view(), name="posts_page"),
   #  path("posts/<slug:slug>", views.post_details, name="post_details_page"),
    path("posts/<slug:slug>", views.PostDetails.as_view(), name="post_details_page"),
    path("form", views.GetPosts.as_view(), name="post_form"),
    path("thank-you", views.thank_you),
]