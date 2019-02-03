from django.shortcuts import render

def index(request) :
    context = {
        "judul" : "Kelas Terbuka",
        "kontributor" : "Faqihza",
    }
    return render(request, "index.html", context)