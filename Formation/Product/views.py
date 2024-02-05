from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request, *args, **kwargs):
    name = "joseph"
    number = 6
    myList = [33, 44, 55, 66]
    context = {
        "name": name,
        "number": number,
        "myList": myList 
    }
    return render(request, 'index.html', context)


def index(request, *args, **kwargs):
    return HttpResponse("hello word")
