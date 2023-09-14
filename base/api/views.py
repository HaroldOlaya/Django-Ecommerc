from django.http import JsonResponse
from ..models import Producto 

def routes(request):
    routes=[
        'GET/api/productos',
        'GET/api/producto/:id'
    ]
    return JsonResponse(routes,safe=False)
def productos (request):
    productos=Producto.objects.all()
    productos_dict=[]
    for p in productos:
        productos_dict.append({
            'nombre': p.nombre,
            'cantidad':p.cantidad, 
            'updated':p.updated
        })
    return JsonResponse(productos_dict,safe=False)
def producto(request,id):
    producto=Producto.objects.get(id=id)
    producto_dict={
        'nombre': producto.nombre,
        'cantidad':producto.cantidad, 
        'updated':producto.updated
    }
    return JsonResponse(producto_dict,safe=False)