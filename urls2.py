from django.conf.urls import url
from django.contrib import admin  

from . import views1

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.about),
    url(r'^$', views.index),
]