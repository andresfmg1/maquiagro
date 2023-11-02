from django.shortcuts import render
from core.models import iconos
from .models import project
from core.models import category

def portafolio(request):
    redes=iconos.objects.all()
    projects=project.objects.all()
    categoria=category.objects.all()
    return  render(request,"portafolio/portafolio.html",{'projects':projects,'redes':redes,'categoria':categoria})