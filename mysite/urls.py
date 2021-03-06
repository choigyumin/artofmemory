# Created by GyuminChoi
# Last modified 2016.8.25

from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import login, logout
from .views import signup
from django.views.generic import TemplateView
from machina.app import board


urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^$', TemplateView.as_view( template_name='intro.html'), name='home'),
    url(r'^admin/', include(admin.site.urls)),
  	url(r'^gallery/', include('AMGallery.urls')),
  	url(r'^source/', include('Source.urls')),
    # Apps
    url(r'^forum/', include(board.urls)),
  	url(r'^accounts/login/', login, name='login' ),
    url(r'^accounts/logout/', logout,
                      {'next_page': '/'}),
    url(r'^accounts/signup/', signup, name='signup'),
    url(r'^signup_ok/$', TemplateView.as_view( \
        template_name='registration/signup_ok.html' \
), name='signup_ok'),
]
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)