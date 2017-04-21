from django import forms

class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
#    c = forms.IntegerField()

# in analysizeTelegram.html
class ExtractForm(forms.Form):
    A4 = BooleanField()
    A5 = BooleanField()
    LocalFile = BooleanField()
    filepath = forms.FilePathField()
