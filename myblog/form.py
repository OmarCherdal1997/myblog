from django import forms
from .models import Post
# class PostForm (forms.Form):
#     title =forms.CharField(max_length=100,label="Your name",error_messages={
#         "required": "Your name must not be empty",
#         "max-length": "Please enter a shorter name"
#     })

#     content= forms.CharField(label="Blog s content",widget=forms.Textarea)
    # date =forms.DateField()
    # author =forms.CharField(max_length=100)

class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = '__all__'
    