from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm
def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            print(name)
            print(email)
    form=ContactForm()
    return render(request, 'form.html', {'form':form})