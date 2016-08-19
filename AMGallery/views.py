from django.utils import timezone
from .models import Work
from django.shortcuts import render, get_object_or_404
from .forms import postForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def work_list(request):
	works = Work.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'AMGallery/work_list.html', {'works':works})
def work_detail(request, pk):
    post = get_object_or_404(Work, pk=pk)
    return render(request, 'AMGallery/post_detail.html', {'post':post})

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
    return render(request, 'AMGallery/post_edit.html', {'form': form})  
