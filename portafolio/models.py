from django.db import models
from django.utils.timezone import now
from core.models import category

class project(models.Model):
    title=models.CharField(max_length=50,verbose_name='Nombre')
    descripcion=models.TextField(verbose_name='Descripcion')
    image=models.ImageField(verbose_name='Imagen',upload_to='projects')
    marca=models.CharField(max_length=50,verbose_name='Marca')
    categories=models.ManyToManyField(category,max_length=20, verbose_name="categoria")
    price=models.FloatField(verbose_name='precio', null=True)
    created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha Creacion') #añade de forma automatica
    updated=models.DateTimeField(auto_now=True,verbose_name="fecha de edicion")
    

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
        ordering=["-created"] #ordena del nuevo al antiguo

    def __str__(self):
        return self.title
