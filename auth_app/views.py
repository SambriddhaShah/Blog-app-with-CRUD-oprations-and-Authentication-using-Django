from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.
def register(request):
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