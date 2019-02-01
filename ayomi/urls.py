from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
	url('', include('django.contrib.auth.urls')),
	url(r'^register/$', views.register, name='register'),
	url(r'^$', views.home, name='home'),
	url(r'^admin/', include(admin.site.urls)),
]
