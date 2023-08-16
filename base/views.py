from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Producto

def home(request):
    productos=Producto.objects.all()
    return render(request,'home.html',{'productos':productos})

def login(request):
    return render(request,'login.html')