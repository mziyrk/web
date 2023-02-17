from django.shortcuts import render
from .models import Todo
# Create your views here.

def h(request):
    return render(request,'a.html')
    


def n(request):
    all = Todo.objects.all()
    return render (request,'b.html',{'todos':all})












