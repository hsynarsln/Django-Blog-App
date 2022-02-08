from django import forms

from blog.models import Post


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'category', 'status')
