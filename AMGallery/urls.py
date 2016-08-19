from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name= 'gallery'
urlpatterns = [
    url(r'^$', views.work_list, name='work_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.work_detail, name='work_detail'),
	url(r'^(?P<pk>[0-9]+)/edit/$', views.work_edit, name='work_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)