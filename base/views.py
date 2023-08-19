from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Marcas,Producto

def home(request):
    marcas=Marcas.objects.all()
    return render(request,'home.html',{'marcas':marcas})

def login(request):
    return render(request,'login.html')

def crear(request):
    return render(request,'crear.html')

def productos(request):
    productos=Producto.objects.all()
    return render (request,'productos.html',{"productos":productos})