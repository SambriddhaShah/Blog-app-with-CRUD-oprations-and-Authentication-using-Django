from django.shortcuts import render,redirect
from content_app.models import Blog

# Create your views here.
def home(request):
    dataset= Blog.objects.all()
    return render(request, 'home.html', {'data':dataset})

def add(request):
    if request. method=='GET':
        return render(request, 'add.html') 
    else:
        t=request.POST['title']
        d=request.POST['description'] 
        Blog.objects.create(title=t, content=d, author_id=request.user.id)  
        return redirect('home')  

def delete(request,id):
    try:
        Blog.objects.get(id=id).delete()
        return redirect('home')
    except:
        return redirect('home')    

def edit(request, id):

    try:
        dataset=Blog.objects.get (id=id)
        if request.method=='GET':
            return render(request, 'edit.html' , {'dataset':dataset})
        else:
            t=request.POST['title']
            d=request.POST['description']
            dataset.title=t
            dataset.content=d
            dataset.save()
            return redirect('home')
           
    except:
        return redirect('edit')



   

def deleteall(request):
    Blog.objects.all().delete()
    return redirect('home')

