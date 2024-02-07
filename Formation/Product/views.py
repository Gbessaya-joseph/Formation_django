from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request, *args, **kwargs):
    myList = [43, 52, 34, 45, 75]
    nom = "joseph"
    return render(request, 'index4.html', {"list": myList, "nom": nom})


def contact(request, *args, **kwargs):
    return render(request, 'Contact.html')

def blog (request, *args, **kwargs):
    return HttpResponse("blog page")
