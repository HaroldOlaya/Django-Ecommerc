from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

from .models import Marcas,Producto

def home(request):
    marcas=Marcas.objects.all()
    return render(request,'home.html',{'marcas':marcas})

def loginPage(request):
    if (request.method== 'POST'):
     username= request.POST.get('username')   
     password= request.POST.get('password')
     if User.objects.filter(username=username).exists():
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
    return render(request,'login.html')

def crear(request,id=None):
    if request.method == "POST":
        id=request.POST.get('id')
        if (id is None):
            Producto.objects.create(
                color=request.POST.get('color'),
                cantidad=request.POST.get('cantidad'),
                nombre=request.POST.get('nombre'),
                imagen=request.POST.get('imagen'),
                precio=request.POST.get('precio')
            )
        else:
            p=Producto.objects.get(id=id)
            p.color=request.POST.get('color')
            p.cantidad=request.POST.get('cantidad')
            p.nombre=request.POST.get('nombre')
            p.imagen=request.POST.get('imagen')
            p.precio=request.POST.get('precio')
            p.save()
    context={}
    if id is not None:
         p=Producto.objects.get(id=id)
         context['producto']=p
    return render(request,'crear.html',context)

def productos(request):
    productos=Producto.objects.all()
    return render (request,'productos.html',{"productos":productos})