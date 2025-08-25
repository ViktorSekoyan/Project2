from django import forms
from .models import Subscribe,Letstalk

class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email2']

class Letstalkform(forms.ModelForm):
    class Meta:
        model = Letstalk
        fields = ['name','email','subject','message']