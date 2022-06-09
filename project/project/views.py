from django.shortcuts import render
from .forms import PersonForm
from database.models import Person, PersonForm

def person_create(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PersonForm()

    return render(request, 'person_create.html', {'form': form})

def person_check(request):
    data = Person.objects.all()
    return render(request, 'person_check.html', {'data': data})