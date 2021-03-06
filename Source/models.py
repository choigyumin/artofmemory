# Created by GyuminChoi
# Last modified 2016.8.25

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey('auth.User', related_name='Post')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title
    def approved_comments(self):
    	return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('Source.Post', related_name='comments')
    author = models.CharField(max_length=200)
    anonymous=models.BooleanField(default=False)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=True)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text