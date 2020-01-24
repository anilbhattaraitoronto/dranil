from django import forms

from .models import Post


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('topic', 'title', 'slug', 'author',
                  'keywords', 'thumbnail', 'content')
