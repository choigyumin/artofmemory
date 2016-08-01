from django.shortcuts import render
from django.utils import timezone
from .models import Work
# Create your views here.
def work_list(request):
	works = Work.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'AMGallery/work_list.html', {'works':works})