from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact

# Create your views here.
def demo(request):
    return HttpResponse("Hello Demo CRUD!!!")

def registerform(request):
    context = {}
    if (request.method == 'POST'):
        context = {
            'success': True,
            'fullname' : request.POST.get('fullname'),
            'email' : request.POST.get('email'),
            'dob' : request.POST.get('dob'),
            'gender' : request.POST.get('gender'),
            'course' : request.POST.get('course'),
        }
    return render(request, 'form.html', context)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        Contact.objects.create(name=name, email=email)
        d = {'name': name, 'email': email}
        return render(request, 'contact.html', d)
    return render(request, 'contact.html')

def contactlist(request):
    contacts = Contact.objects.all()
    return render(request, 'contactlist.html', {'contacts': contacts})