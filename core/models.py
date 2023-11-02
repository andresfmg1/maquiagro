from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class category(models.Model):
    name = models.CharField(max_length=50,verbose_name="Nombre")
    created = models.DateTimeField(auto_now=True,verbose_name="fecha de creacion")
    update = models.DateTimeField(auto_now=True,verbose_name="fecha de edicion")

    class meta: 
        verbose_name="categoria"
        verbose_name_plural="categorias"
        ordering=["-created"]
    def __str__(self):
        return self.name
    

# Create your models here.
class iconos(models.Model):
    title=models.CharField(max_length=100,verbose_name='Titulo')
    icono = models.CharField(max_length=100)
    link=models.URLField(verbose_name='Link', null=True,blank=True)
    published=models.DateTimeField(default=now,verbose_name="fecha de publicacion")
    autor= models.ForeignKey(User, on_delete=models.CASCADE,null=True,verbose_name="autor")
    created=models.DateTimeField(auto_now_add=True,verbose_name='Fecha creacion') #añade la fecha actual #automatica
    update=models.DateTimeField(auto_now=True,verbose_name='Fecha actualizado')
    
    class Meta:
        verbose_name="Icono"
        verbose_name_plural="Iconos"
        ordering=["-created"]
    def __str__(self):
        return self.title 
    


# Create your models here.
class pagina(models.Model):
    title= models.CharField(max_length=100,verbose_name="Titulo")
    contenido=RichTextField(verbose_name='contenido')
    orden=models.SmallIntegerField(verbose_name='order',default=0)
    created= models.DateTimeField(auto_now_add=True, verbose_name="fecha de creacion")
    update= models.DateTimeField(auto_now=True, verbose_name="fecha de edicion")
    
    class Meta: 
        verbose_name="Pàgina"
        verbose_name_plural="Pàginas"
        ordering=["-created"]
    def __str__(self):
        return self.title
