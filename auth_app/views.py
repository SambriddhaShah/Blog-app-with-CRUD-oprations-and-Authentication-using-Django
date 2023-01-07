from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):


    try:
        if request.method=='GET':
            return render(request, 'register.html')
        else:
            fn=request.POST['firstname']
            ln= request.POST['lastname']
            email=request.POST['email']
            usern=request.POST['username']
            paswd=request.POST['password']

            User.objects.create_user(first_name=fn, last_name=ln, email=email, username=usern, password=paswd)
            return redirect('home')
    except:
        return redirect('register')

   



def signin(request):

    if request.method=='GET':
        return render(request, 'login.html')
    else:
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('signin')  


def logout_view(request):
    logout(request)
    return redirect('signin')
    