from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="main_page"),
    path("posts", views.posts, name="posts_page"),
    path("posts/<slug:slug>", views.post_details, name="post_details_page"),
    path("form", views.get_posts, name="post_form"),
    path("thank-you", views.thank_you),
]