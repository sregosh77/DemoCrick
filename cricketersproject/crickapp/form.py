from django import forms
from. models import Cricketers
class Cricketersform(forms.ModelForm):
    class Meta:
        model=Cricketers
        fields=['name','skill','year','img']
