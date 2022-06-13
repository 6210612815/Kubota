from django import forms

class PersonForm(forms.Form):
    employee_id = forms.IntegerField(label='employee_id')
    card_id = forms.IntegerField(label='card_id')

class ResetForm(forms.Form):
    pass_1st = forms.IntegerField(label='pass_1st')
    pass_2nd = forms.IntegerField(label='pass_2nd')