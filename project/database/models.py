from django.db import models
from django import forms

# Create your models here.
class Email(models.Model):
    email = models.CharField(max_length=100)

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = '__all__'
        label = {
            'email' : 'อีเมล'
        }
