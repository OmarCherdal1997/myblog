from django.db import models

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=50)
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email      = models.EmailField( max_length=254)

class Post(models.Model):
    author = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=150)
    image   = models.CharField(max_length=50)
    date    = models.DateField(auto_now=False, auto_now_add=False)
    slug    = models.SlugField()
    content = models.TextField()
    author  = models.ForeignKey(Author, on_delete=models.SET_NULL)
    tag     = models.ManyToManyField(Tag)