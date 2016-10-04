from django import forms
from .models import Post, Tag

class PostForm(forms.ModelForm):
    tag = forms.CharField(
        label='Tag',
        help_text='The tag you want to use for your post',
    )

    class Meta:
        model = Post
        fields = ('title', 'content', 'published')
