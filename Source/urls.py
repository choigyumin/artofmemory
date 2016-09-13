# Created by GyuminChoi
# Last modified 2016.8.25

from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
	url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
	url(r'^(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^(?P<pk>[0-9]+)/p_remove/$', views.output_post_remove, name='output_post_remove'),
	url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
	url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.source_comment_remove, name='source_comment_remove'),
	url(r'^post/(?P<pk>[0-9]+)/edit/$', views.source_comment_edit, name='source_comment_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)