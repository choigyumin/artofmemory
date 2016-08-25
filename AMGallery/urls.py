# Created by GyuminChoi
# Last modified 2016.8.25

from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.work_list, name='work_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.work_detail, name='work_detail'),
	url(r'^(?P<pk>[0-9]+)/edit/$', views.work_edit, name='work_edit'),
	url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_work, name='add_comment_to_work'),
	url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)