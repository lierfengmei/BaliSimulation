from django import forms

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
#    c = forms.IntegerField()

# in analysizeTelegram.html
class ExtractForm(forms.Form):
    A4接口 = forms.BooleanField(initial=True)
#    option1 = forms.BooleanField(initial=True)
#    optionsRadios1 = forms.BooleanField(initial=True)
    A5接口 = forms.BooleanField(initial=True)
    选择本地报文 = forms.BooleanField(initial=True)  
#   LocalFile =forms. BooleanField(initial=True)
    filepath = forms.FilePathField(path="e://read.txt")
