from django.http import HttpResponse 

def index(request) :  
    # Dalam HttpResponse dapat dimasukkan HTML
    # return HttpResponse("<h1> Ini Adalah Home </h1>")
    
    # Atau dapat dimasukkan variabel tapi tidak disarankan membuat HTML pada file ini
    judul = "<h1> Ini Adalah Home </h1>"
    subjudul = "<h2> Selamat datang di website ini </h2>"
    output = judul + subjudul
    return HttpResponse(output)

def about(request) :  
    return HttpResponse("<h1> Ini Adalah About </h1>")