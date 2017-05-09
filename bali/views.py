from django.shortcuts import render
from django.http import HttpResponse

from .forms import AddForm
from .forms import ExtractForm
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

#----------写入报文处理函数--------------------------
def writeBalise(request):
   # json_receive = json.loads(request.body)
   # name = json_receive['name']
   # age = json_receive['age']
    return render(request,'bali/writeBalise.html',{})

def writeTele(request):
    write_tele = request.GET['write_tele']
    # todo!这个地方处理传过来的write_tele写入报文，然后往下位机写入报文，
    # 根据写入是否成功，来向网页前端传送是否写入成功的标志！
    if write_tele:
        writeResult = write_tele+"\nWrite Telegram Success!"
    else:
        writeResult = write_tele+"\n Write Telegram Failed!"
    return HttpResponse(writeResult)
#----------------------------------------------------



def readLEU(request):
    return render(request,'bali/readLEU.html',{})

def writeLEU(request):
    return render(request,'bali/writeLEU.html',{})

def generateTelegram(request):
    return render(request,'bali/generateTelegram.html',{})

#----------------解析报文处理函数-----------------------
def analysizeTelegram(request):
    return render(request,'bali/analysizeTelegram.html',{})


def extractTele(request):
    choice = request.GET['choice']
    localTelegram = request.GET['localTelegram']
    if choice=='A4':
        #todo,here get A4 read telegram
        telegram = 'A4 Read Telegram'
    elif choice=='A5':
        #todo,here get A5 read telegram
        telegram = 'A5 Read Telegram'
    else:
        telegram = localTelegram
    return HttpResponse(telegram)

def analysizeTele(request):
    telegram = request.GET['telegram']
    #todo,call python to analysize telegram
    analysizeResult = telegram
    return HttpResponse(analysizeResult)

#
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


#def analysizeTelegram1(request):
#    if request.method =='post':
#        form = ExtractForm(request.POST)
#        if form.is_valid():
#            isA4 = form.cleaned_data['optionsRadios1']    
#            isA5 = form.cleaned_data['option2']
#            isLocalFile = form.cleaned_data['option3']  
#            filepath = "e://read.txt" #modify            
#    else:
#        form = ExtractForm()
#    return render(request,'bali/analysizeTelegram.html',{'form':form})

#def analysizeTelegram(request):
#    if request.method == 'POST':
       # extract_tele = 'This is extract data'
#        analyse_tele = 'This is analysize_data'
#        choice = 'This is extract data'
#    else:
#        choice = request.GET.get('option', 'No option get!')
#        extract_tele='这里显示提取报文的结果'
#        analyse_tele='这里显示解析报文的结果'
#    return render(request,'bali/analysizeTelegram.html',{'choice':choice,'analyse_tele':analyse_tele})
#----------------------------------------------------------------


 #  return render(request,'bali/analysizeTelegram.html',{})

def testBaliseSwitch(request):
    return render(request,'bali/testBaliseSwitch.html',{})

def testBaliseNoSwitch(request):
    return render(request,'bali/testBaliseNoSwitch.html',{})

def test(request):
    return render(request,'bali/test.html',{})

def about(request):
    return render(request,'bali/about.html',{})


