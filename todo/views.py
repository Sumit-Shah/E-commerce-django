from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    people=[
        {
            'name':"Sumit",
            'age':25,
            'gender':'Male'
        },
        {
            'name':"Santosh",
            'age':22,
            'gender':'Male'
        },
        {
            'name':"Rajni",
            'age':26,
            'gender':'Female'
        }
    ]
    
    context={
        'people':people
    }
    return render(request, 'index.html',context)

def about_us(request):
    return render(request,'about_us.html')