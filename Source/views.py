# Created by GyuminChoi
# Last modified 2016.8.25

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post,Comment
from .forms import postForm, CommentForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

def post_list(request):
	post = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'Source/post_list.html', {'post' : post})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'Source/post_detail.html', {'post': post})

def post_new(request):
	if request.method == "POST":
		form = postForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return render(request, 'Source/post_detail.html', {'post':post})    
	else:
		form = postForm()
	return render(request, 'Source/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = postForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('Source.views.post_detail', pk=post.pk)
    else:
        form = postForm(instance=post)
    return render(request, 'Source/post_edit.html', {'form': form})  

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author=request.user
            comment.post = post
            comment.save()
            return redirect('Source.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'Source/add_comment_to_post.html', {'form': form})

@login_required
def source_comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('Source.views.post_detail', pk=post_pk)