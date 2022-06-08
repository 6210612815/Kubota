from django.shortcuts import render
from database.models import Email, EmailForm

def index(request):
    data_email = ['sittichok','kotcharkorn','pornlapus']
    if 'email' not in data_email:
        return render(request, 'index.html')
    else:
        data = {
            'email' : request.POST.get('email',None),
        }
        return render(request, 'noEmail.html', data)

"""
def index(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = EmailForm()
    
    return render(request, 'index.html', {'form': form})
"""