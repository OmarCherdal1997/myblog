from django.contrib import admin
from myblog.models import Tag,Author,Post

# Register your models here.
# 
class PostAdmin(admin.ModelAdmin):
    list_filter = ("author","tag","date",)
    list_display = ("title","author","date",)
    prepopulated_fields = {"slug":("title",)}

admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)

