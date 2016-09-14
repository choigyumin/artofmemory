#-*- coding: utf-8 -*-
# Created by GyuminChoi
# modified 2016.8.25
# modified 2016.9.14


from django.utils import timezone
from .models import Work,Comment
from django.shortcuts import render, get_object_or_404
from .forms import postForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import postForm, CommentForm
from django.contrib.auth.decorators import login_required



def work_list(request):
	works = Work.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'AMGallery/work_list.html', {'works':works})
def work_detail(request, pk):
    post = get_object_or_404(Work, pk=pk)
    return render(request, 'AMGallery/work_detail.html', {'post':post})

def work_edit(request, pk):
    post = get_object_or_404(Work, pk=pk)
    if request.method == "POST":
        form = postForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('AMGallery.views.work_detail', pk=post.pk)
    else:
        form = postForm(instance=post)
    return render(request, 'AMGallery/work_edit.html', {'form': form})  

def output_work_remove(request, pk):
    post = get_object_or_404(Work, pk=pk)
    post.delete()
    return redirect('AMGallery.views.work_list')

def add_comment_to_work(request, pk):
    post = get_object_or_404(Work, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            if comment.anonymous :
                comment.author = "익명"
            else :
                comment.author=request.user
            comment.save()
            return redirect('AMGallery.views.work_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'AMGallery/add_comment_to_work.html', {'form': form})


def comment_edit(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post=post
            if comment.anonymous :
                comment.author = "익명"
            else :
                comment.author = request.user
            comment.save()
            return redirect('AMGallery.views.work_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'AMGallery/comment_edit.html', {'form': form})  

@login_required
def output_comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('AMGallery.views.work_detail', pk=post_pk)

