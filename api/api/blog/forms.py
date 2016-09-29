from django import forms
from .models import Post, Tag

class PostForm(forms.ModelForm):
    tag = forms.CharField(
    )

    class Meta:
        model = Post
        fields = ('title', 'content', 'published')
