from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import requests
# Create your views here.

from .models import Marcas,Producto,Pago

def api(request):

    url = "https://car-data.p.rapidapi.com/cars"

    querystring = {"limit":"30","page":"0"}

    headers = {
        "X-RapidAPI-Key": "1e21636f54msh6fa12f156e85130p1b551ajsndc63a52bfaf8",
        "X-RapidAPI-Host": "car-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    datos=response.json()
    print(type(datos))
    print(datos)
    return render(request,'api.html',{'datos':datos})
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
def logoutPage(request):
    logout(request)
    return redirect("/")

def registro (request):
    if (request.method=="POST"):
        username=request.POST.get("username")
        nombre=request.POST.get("nombre")
        email=request.POST.get("email")
        contraseña=request.POST.get("contraseña")
        confirmar_contraseña=request.POST.get("confirmar_contraseña")
        if(contraseña==confirmar_contraseña):
            User.objects.create_user(username,first_name=nombre,email=email,password=contraseña)
        return redirect ('/login')
    return render(request,'registro.html')
def crear(request,id=None):
    if request.method == "POST":
        id=request.POST.get('id')
        if (id is None):
            Producto.objects.create(
                color=request.POST.get('color'),
                cantidad=request.POST.get('cantidad'),
                nombre=request.POST.get('nombre'),
                imagen=request.POST.get('imagen'),
                precio=request.POST.get('precio'),
                user=request.user
            )
            return redirect('/productos')
        else:
            p=Producto.objects.get(id=id)
            if (p.user== request.user):
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
    productos=Producto.objects.order_by('-updated')
    return render (request,'productos.html',{"productos":productos})

def compra(request):
    if request.method == "POST":
        Pago.objects.create(
            numeroFactura=request.POST.get('factura'),
            valor=request.POST.get('precio')
        )
        return redirect('/productos')
    return render(request,'comprar.html')