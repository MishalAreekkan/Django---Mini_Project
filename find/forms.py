from django.forms import ModelForm
from django import forms
from .models import Vehicle_type

class Vehicleform(ModelForm):
    class Meta:
        model = Vehicle_type
        fields = ('name','register_no','owner','model','notes','image')
        
class Searching(forms.Form):
    search = forms.CharField(label="SEARCH",max_length=100)