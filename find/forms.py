from django.forms import ModelForm
from .models import Vehicle_type

class Vehicleform(ModelForm):
    class Meta:   ## main's class decribe/ main class properties
        model = Vehicle_type
        fields = '__all__'
        # app_label = 'find'