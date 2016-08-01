from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.work_list, name='work_list'),
]