from django.shortcuts import render,HttpResponse,redirect
from.models import Task
# Create your views here.
def index(request):
    tasks=Task.objects.all()
    context={
        'tasks':tasks
    }
    return render(request, 'index.html',context)


def create(request):
    if request.method == "POST":
        title=request.POST.get('title')
        description=request.POST.get('description')
        
        if title == "" or description == "":
            context={
                'error':'Both field are required.'
            }
            return render(request, 'create.html',context)
        
        
        Task.objects.create(name=title, description=description)
        return redirect("/")
    
    return render(request, 'create.html')
    
    
def about_us(request):
    return render(request,'about_us.html')