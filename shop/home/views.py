from django.shortcuts import render
from .models import Todo


# Create your views here.


def say_hello(request):
    return render(request ,'home.html')

def home(request):
    all = Todo.objects.all()
    return render(request,'home.html',{'todos':all})