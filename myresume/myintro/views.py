from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login

# Create your views here.
def index(request):
    context={
        'category': 'Academic'
    }
    if request.user.is_anonymous:
        return redirect('/login')
        # return HttpResponse('This is index page')
    return render(request, 'index.html', context)

def contact(request):
    context={
        'category': 'Contact'
    }
    return render(request, 'contact.html', context)

def service(request):
    return HttpResponse('This is our services')


def loginUser(request):
    if request.method == "POST":
        #check if user has correct credentials
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("/")#redirect to home page if user exist
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html')
            
    return render(request, 'login.html')



def logoutUser(request):
    logout(request)
    return redirect("/login")