from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.

def index(request):
    context = {
        "variable":"You can do it"
    }
    return render(request, 'index.html', context)


def about(request):
    return HttpResponse("this is about page")

def services(request):
    return HttpResponse("this is services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        contact = Contact(name=name, email=email, phone=phone, message=message, date= datetime.today())
        print(message, 'hellp')
        contact.save()
    return render(request, 'contact.html')