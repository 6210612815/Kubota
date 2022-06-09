from django import forms
class PersonForm(forms.Form):
    employee_id = forms.IntegerField(label='employee_id')
    card_id = forms.IntegerField(label='card_id')