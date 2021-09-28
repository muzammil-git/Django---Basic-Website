from django.shortcuts import render, HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages


# Create your views here.
def index(request):

    context ={
        'name':"Muzammil",
        'age':"22",
        'mentor':"Sir Amir"
    }

    # messages.success(request, "This is a success")
    return render(request,'index.html', context)    #request, template, variables

    # return HttpResponse("this is homepage")

def product(request):
    return render(request,'products.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request,  'Feedback has been recorded!')

    return render(request,'contacts.html')
