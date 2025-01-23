from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!!!")

def misha(request):
    return HttpResponse("Hello, Misha")

def david(request):
    return HttpResponse("Hello, David")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")

def html_doc(request):
    return render(request, "hello/index.html")
# we must create "templates" folder inside "hello" folder and then index.html inside folder "hello"

def greet1(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })