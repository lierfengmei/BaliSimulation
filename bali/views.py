from django.shortcuts import render
from django.http import HttpResponse
import ctypes
import sys

from .forms import AddForm
from .forms import ExtractForm

#调用函数
from .callfunc import *

so = ctypes.cdll.LoadLibrary
decodelib = so("./PyDecode/libDecode.so")

def show_data(request):
    if request.method == 'post':
        show_data = "This is the second default show data"
    else:
        form = ExtractForm()
    return render(request,'bali/readBalise.html',)

def index(request):
    return render(request,'bali/index.html',{})


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
#---------读取报文处理函数---------------------------

def readBalise(request):
    return render(request,'bali/readBalise.html',{})

def readTele(request):
    choice = request.GET['choice']
    if choice=='A4':
        #todo,here get A4 read telegram
        readTelegram = 'A4 Read Telegram'
    else:
        #todo,here get A5 read telegram
        readTelegram = 'A5 Read Telegram'
    return HttpResponse(readTelegram)

def compareTele(request):
    readTelegram = request.GET['readTelegram']
    compareTelegram = request.GET['compareTelegram']
    if readTelegram==compareTelegram:
        compareResult = "The telegrams are the same!"
    else:
        compareResult = "The telegram are not the same!"
    return HttpResponse(compareResult)

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

#--------写LEU相关函数-------------------------------

def writeLEU(request):
    return render(request,'bali/writeLEU.html',{})

def writeTE1(request):
    write_tele = request.GET['write_tele']
    #todo 把write_tele写入到LEU中并获取返回成果
    Result = "TE1 write Success!"
    return HttpResponse(Result)

def writeTPC(request):
    write_tele = request.GET['write_tele']
    #todo 把write_tele写入到LEU中并获取返回成果
    Result = "TPC write Success!"
    return HttpResponse(Result)

def writeTSE(request):
    write_tele = request.GET['write_tele']
    #todo 把write_tele写入到LEU中并获取返回成果
    Result = "TSE write Success!"
    return HttpResponse(Result)

#--------------------------------------------------



def readLEU(request):
    return render(request,'bali/readLEU.html',{})
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

    #todo test to call python function
    a = Sum(20)
    analysizeResult+=str(a)
    tele_ori=" 98 3B E6 32 7B 23 75 ED 96 19 46 9A 3D 0E F2 A6 3D 2D 7C 37 88 CD F7 77  C3 DD EB D1 82 65 A7 F5 22 D4 BB D4 75 3A DC 4D 34 2F 5E 63 91 C7 B3 92 96 BA 7D 7B EC DB 14 2F 24 5C 87 F8 EA 7D 3E 0D 2B F6 F2 F1 AB 99 5B 7E DF 45 3C 41 3C AE 77 C2 3B E9 7C 47 5A 7D F2 C5 5D 49 AA F3 30 6774 FC4A C7 59 F2 D9 ED 5E F9 13 E2 E6 17 85 92 CD 7B 0F D9 10 1B 51 67 29 2F  B5 DF 89 B8 AC DE DA 7C";
    decodelib.Decode(tele_ori)

    b = sys.stdout.read()

    analysizeResult+=str(b)

    return HttpResponse(analysizeResult)
#----------------------------------------------------------------

def testBaliseSwitch(request):
    return render(request,'bali/testBaliseSwitch.html',{})

def testBaliseNoSwitch(request):
    return render(request,'bali/testBaliseNoSwitch.html',{})

def test(request):
    return render(request,'bali/test.html',{})

def about(request):
    return render(request,'bali/about.html',{})


