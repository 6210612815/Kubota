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

class Reset(models.Model):
    pass_1st = models.CharField(max_length=100)
    pass_2nd = models.CharField(max_length=100)

class ResetForm(forms.ModelForm):
    class Meta:
        model = Reset
        fields = '__all__'
        label = {
            'pass_1st' : 'รหัสผ่านใหม่',
            'pass_2nd' : 'ยืนยันรหัสผ่านใหม่',
        }