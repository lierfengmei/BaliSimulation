from django.shortcuts import render
from django.http import HttpResponse

from .forms import AddForm
from .forms import ExtractForm

#in analysizeTelegram.html, to extract and analysize the telegram
#def myextract_tele(request):
#    if request.method =='post':
#        form = ExtractForm(request.POST)
#        if form.is_valid():
#            isA4 = False     
#            isA5 = False 
#            isLocalFile = True  
#            filepath = "e://read.txt" #modify            
#    else:
#        form = ExtractForm()
#    return render(request,'bali/analysizeTelegram.html',{'form':form})


def extract_tele(request):
    if request.method == 'post':
        form = ExtractForm(request.POST)
        if form.is_valid():
            # todo ! to modify
            extract_tele = "This is default telegram"
            return render(request,'bali/analysizeTelegram.html',{'extract_tele':extract_tele,'form':form})
    else:
        form = ExtractForm()
    return render(request,'bali/analysizeTelegram.html',{'form':form})

def show_data(request):
    if request.method == 'post':
        show_data = "This is the second default show data"
    else:
        form = ExtractForm()
    return render(request,'bali/readBalise.html',)

def index(request):
    return render(request,'bali/index.html',{})


def addAandB(a,b):
    pass

def minusAandB():
    pass

def add(request):
  #  show_data = "This is my default show data"
    if request.method == 'POST':#提交表单时
        myform = AddForm(request.POST) #form包含提交的数据
        if myform.is_valid():
            a = myform.cleaned_data['a']
            b = myform.cleaned_data['b']
#            if request.POST.has_key('add'):
            if 'add' in request.POST:   #加法
                data=str(int(a)+int(b))
            else:
                data=str(int(a)-int(b)) #减法
    #        return render(request,'bali/readBalise.html',{'data':data,'myform':myform,'show_data':show_data})
            return render(request,'bali/readBalise.html',{'data':data,'myform':myform})
            #return HttpResponse(str(int(a)+int(b)))
    else:#当正常访问时
        myform = AddForm()
    #return render(request,'bali/readBalise.html',{'myform':myform,'show_data':show_data})
    return render(request,'bali/readBalise.html',{'myform':myform})


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

def analysizeTelegram1(request):
    if request.method =='post':
        form = ExtractForm(request.POST)
        if form.is_valid():
            isA4 = form.cleaned_data['optionsRadios1']    
            isA5 = form.cleaned_data['option2']
            isLocalFile = form.cleaned_data['option3']  
            filepath = "e://read.txt" #modify            
    else:
        form = ExtractForm()
    return render(request,'bali/analysizeTelegram.html',{'form':form})

def analysizeTelegram(request):
    if request.method == 'POST':
       # extract_tele = 'This is extract data'
        analyse_tele = 'This is analysize_data'
        choice = 'This is extract data'
    else:
        choice = request.GET.get('option', 'No option get!')
#        extract_tele='这里显示提取报文的结果'
        analyse_tele='这里显示解析报文的结果'
    return render(request,'bali/analysizeTelegram.html',{'choice':choice,'analyse_tele':analyse_tele})



 #  return render(request,'bali/analysizeTelegram.html',{})

def testBaliseSwitch(request):
    return render(request,'bali/testBaliseSwitch.html',{})

def testBaliseNoSwitch(request):
    return render(request,'bali/testBaliseNoSwitch.html',{})

def test(request):
    return render(request,'bali/test.html',{})

def about(request):
    return render(request,'bali/about.html',{})


