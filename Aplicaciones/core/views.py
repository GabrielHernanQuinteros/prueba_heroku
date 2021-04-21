from django.shortcuts import render

from django.shortcuts import HttpResponse

# Create your views here.

def home(request):
    return render(request, "core/home.html")
    #return HttpResponse("<h1>Mi Web Personal</h1><h2>Portada</h2>")

    