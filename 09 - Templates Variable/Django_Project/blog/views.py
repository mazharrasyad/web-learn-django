from django.shortcuts import render

# Create your views here.

def index(request) :
    context = {
        "judul" : "Blog",
        "kontributor" : "Budi",
    }
    return render(request, "blog/index.html", context)

def news(request) :
    context = {
        "judul" : "News",
        "kontributor" : "Rudi",
    }
    return render(request, "blog/index.html", context)

def cerita(request) :
    context = {
        "judul" : "Cerita",
        "kontributor" : "Abdi",
    }
    return render(request, "blog/index.html", context)