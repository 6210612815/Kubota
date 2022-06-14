from django.shortcuts import render
from .forms import PersonForm, ResetForm
from database.models import Person, PersonForm, Reset, ResetForm

def index(request):
    return render(request, 'person_create.html')

# หน้ากรอก รหัสพนักงาน
def person_create(request): 
    
    # connect API
    # Get token => Send username password 
    # Get Employee data => Accesstoken url


    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PersonForm()

    return render(request, 'person_create.html', {'form': form})

# 
def person_created(request):
    data = Person.objects.all()
    return render(request, 'person_created.html', {'data': data})


def reset_password(request):
    if request.method == "POST":
        form = ResetForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ResetForm()

    return render(request, 'reset_password.html', {'form': form})

def reset_success(request):
    data = Reset.objects.all()
    return render(request, 'reset_success.html', {'data': data})