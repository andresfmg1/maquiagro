from django.shortcuts import render
from .models import iconos,pagina
from Servicio.models import Servicio
from portafolio.models import project
from .models import category
from carrito.carrito import carrito

# Create your views here.

def inicio(request):
    carro=carrito(request)
    redes=iconos.objects.all()
    servicios=Servicio.objects.all()
    pagi=pagina.objects.all()
    return  render(request,"core/inicio.html",{'redes':redes,'servicios':servicios,'pagi':pagi})

def servicio(request):
    return  render(request,"core/servicio.html",)

def contacto(request):
    redes=iconos.objects.all()
    servicios=Servicio.objects.all()
    return  render(request,"core/contacto.html",{'redes':redes,'servicios':servicios})
    
def registro(request):
    redes=iconos.objects.all()
    return  render(request,"registro/registro.html",{'redes':redes})

def producto(request):
    projects=project.objects.all()
    redes=iconos.objects.all()
    categoria=category.objects.all()
    return  render(request,"core/productos.html",{'projects':projects,'redes':redes,'categoria':categoria})