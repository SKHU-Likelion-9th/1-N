from django import forms
from .models import Post#,Comment 추가

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'writer', 'body']

# CommentForm 작성