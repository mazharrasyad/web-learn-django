from django.conf.urls import url
from django.contrib import admin  

""" 
1. Code dibawah ini tidak efektif karena jika ada banyak views menjadi tidak terstruktur
Solusinya perlu dibuat file view baru untuk menampung fungsi-fungsi tersebut
Contoh views.py

from django.http import HttpResponse 

def index(request) :  
    return HttpResponse("Assalamu'alaikum")  

def about(request) :  
    return HttpResponse("Ini About")  
"""

"""
2. Code dibawah ini juga tidak efektif karena jika ada nama function yang sama akan bertabrakan
from .views import index, about
from .views2 import index
"""

# 3. Berikut solusi agar views menjadi efektif
from . import views

# Kemudian pada urlpatterns tambahkan nama file pada masing-masing function

""" Sebelum
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', about),  
    url(r'^$', index), # Home
]
"""

# Sesudah
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.about),
    url(r'^$', views.index),
]