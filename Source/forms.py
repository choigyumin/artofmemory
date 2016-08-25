# Created by GyuminChoi
# Last modified 2016.8.25

from django import forms
from .models import Post, Comment

class postForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)