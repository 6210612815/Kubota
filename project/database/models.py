from django.db import models
from django import forms

# Create your models here.
class Person(models.Model):
    employee_id = models.IntegerField()
    card_id = models.IntegerField()

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        label = {
            'employee_id' : 'รหัสพนักงาน',
            'card_id' : 'เลขบัตรประชาชน',
        }
