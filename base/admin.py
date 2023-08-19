from django.contrib import admin

# Register your models here.


from .models import Producto,Promocion,Marcas

admin.site.register(Producto)
admin.site.register(Promocion)
admin.site.register(Marcas)