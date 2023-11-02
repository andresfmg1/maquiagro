from django.db import models

# Create your models here.
class Servicio(models.Model):
    title = models.CharField(max_length=100,verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image=models.ImageField(verbose_name='Imagen',upload_to='Servicio')
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creaciòn")#añade la fecha actual
    updated = models.DateTimeField(auto_now=True)#actualizar la fecha actual
    price = models.FloatField(max_length=20, verbose_name='precio', blank=True, null=True)
    class Meta:
        verbose_name="Servicio"
        verbose_name_plural="Servicios"
        ordering=["-created"]
    def __str__(self):
        return self.title