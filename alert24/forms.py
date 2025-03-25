from django import forms

class Students(forms.Form):
    names = forms.CharField(widget = forms.FileInput) 
    email = forms.EmailField(widget= forms.EmailInput(
        attrs = {
            "placeholder":"Enter your massage....",
            "type":"date",
            "class": 'form-control bg-success-subtel'
        }
    ))


    email = forms.CharField()
    message = forms.CharField()