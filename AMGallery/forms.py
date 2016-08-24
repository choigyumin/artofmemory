from django import forms
from .models import Work, Comment

class postForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
