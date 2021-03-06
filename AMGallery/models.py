# Created by GyuminChoi
# Last modified 2016.8.25

from django.db import models
from django.utils import timezone

class Work(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    anonymous=models.BooleanField(default=False)
    image = models.FileField()
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def approved_comments(self):
    	return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('AMGallery.Work', related_name='comments')
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
