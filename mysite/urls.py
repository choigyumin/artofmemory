from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import login, logout

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
  	url(r'^gallery/', include('AMGallery.urls')),
  	url(r'^source/', include('Source.urls')),
  	url(r'', include('AMGallery.urls')),
  	url(r'^accounts/login/', login, name='login' ),
    url(r'^accounts/logout/', logout, name='logout' ),
]
urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)