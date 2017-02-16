from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'bali/index.html',{})


def faq(request):
    return render(request,'bali/faq.html',{})

def intro(request):
    return render(request,'bali/intro.html',{})

def operation(request):
    return render(request,'bali/operation.html',{})

def readBalise(request):
    return render(request,'bali/readBalise.html',{})

def test(request):
    return render(request,'bali/test.html',{})


