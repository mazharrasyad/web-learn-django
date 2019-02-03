from django.conf.urls import urls

from . import views

urlpatterns = [
    url(r'^recent/$', views.recent),
    url(r'^$', views.index),
]