from django.db import models
from django.utils.text import slugify

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=50)
    def __str__(self):
        return self.caption
    
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email      = models.EmailField( max_length=254)
    def __str__(self) -> str:
        return f"{self.first_name}  {self.last_name}"

class Post(models.Model):
    title   =  models.CharField(max_length=100, null=True)
    author  = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=250)
    image   = models.CharField(max_length=50)
    date    = models.DateField(auto_now=False, auto_now_add=False)
    slug    = models.SlugField(unique=True,db_index=True)
    content = models.TextField()
    author  = models.ForeignKey(Author,null=True ,on_delete=models.SET_NULL
        ,related_name="posts")
    tag     = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.title

    # def __save__ (self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super(Post, self).save(*args, **kwargs)