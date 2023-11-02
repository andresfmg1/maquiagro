from django.shortcuts import render
from .carrito import carrito
from portafolio.models import project
from django.shortcuts import redirect

# Create your views here.

def agregar_producto(request,producto_id):
    carro=carrito(request)
    producto=project.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("portafolio")

def eliminar_producto(request,producto_id):
    carro=carrito(request)
    producto=project.objects.get(id=producto_id)
    carro.eliminar(producto=producto) #solo se cambia la funcion agregar por la de eliminar que se creo en models.py
    return redirect("portafolio")

def restar_producto(request,producto_id):
    carro=carrito(request)
    producto=project.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("portafolio")

def limpiar_carro(request):

    carro = carrito(request)

    carro.limpiar_carro()

    return redirect("portafolio")

