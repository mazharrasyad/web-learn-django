from django.http import HttpResponse
from django.shortcuts import render # Mengambil file template

def index(request) :
    return render(request, "index.html")    
    # argument 1 : request untuk mengambil file dari folder tempalte
    # argument 2 : file pada folder template

def about(request) :  
    return render(request, "about.html")