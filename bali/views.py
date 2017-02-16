from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index1(request):
    return HttpResponse("Here is the index page!")

def index(request):
    return render(request,'base_rango.html',{})
