from django import forms

from .models import Work

class postForm(forms.ModelForm):

    class Meta:
        model = Work
        fields = ('title', 'text',)