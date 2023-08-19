from django.db import models

# Create your models here.

class Producto(models.Model):
    color = models.CharField(max_length=200)
    nombre = models.TextField()
    cantidad = models.PositiveIntegerField()
    updated = models.DateField(auto_now=True)
    imagen = models.TextField()
    precio= models.PositiveIntegerField()
    
    def __str__(self):
        return  self.nombre
    
class Promocion(models.Model):
    nombre= models.TextField()
    precioAnterior= models.IntegerField()
    precionAhora = models.IntegerField()
    fechaLimite=models.DateField()
    
    def __str__(self):
        return ("Nombre del producto: "+self.nombre)
    
class Marcas(models.Model):
    nombre=models.TextField()
    logo=models.TextField()
    
    def __str__(self):
        return(self.nombre)
    
