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

def writeBalise(request):
    return render(request,'bali/writeBalise.html',{})

def readLEU(request):
    return render(request,'bali/readLEU.html',{})

def writeLEU(request):
    return render(request,'bali/writeLEU.html',{})

def generateTelegram(request):
    return render(request,'bali/generateTelegram.html',{})

def analysizeTelegram(request):
    return render(request,'bali/analysizeTelegram.html',{})

def testBaliseSwitch(request):
    return render(request,'bali/testBaliseSwitch.html',{})

def testBaliseNoSwitch(request):
    return render(request,'bali/testBaliseNoSwitch.html',{})

def test(request):
    return render(request,'bali/test.html',{})

def about(request):
    return render(request,'bali/about.html',{})


