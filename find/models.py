from django.db import models

# Create your models here.

class Vehicle_type(models.Model):
    name = models.CharField(max_length=250)
    owner = models.CharField(max_length=250)
    model = models.IntegerField(null=True)
    notes = models.TextField
    
