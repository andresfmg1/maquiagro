from django.shortcuts import render,redirect
from core.models import iconos
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

def contacto(request):
    contacto_formulario = ContactForm() #se instancia para enviarlo e un diccionario 
    if request.method == 'POST':
        contacto_formulario = ContactForm (data=request.POST)
        if contacto_formulario.is_valid():
            nombre = request.POST.get('nombre', '')
            correo = request.POST.get('correo', '')
            contenido = request.POST.get('contenido', '')
            correo = EmailMessage(
                "Maquiagro",
                "De {} <{}>\n\nEscribió:\n\n{}".format(nombre, correo,contenido),
                "stmp.gmail.com",
                ["julitmacias2004@gmail.com"],
                reply_to= [correo]
            )
            try:
                correo.send()
                # este el mensaje que envia en el caso de que todo se encuentre correctamente
                return redirect(reverse('contacto')+"?ok")
            except:
                #error que direcciona a un fallo
                return redirect(reverse('contacto')+"?fail")
        return redirect(reverse('contacto')+"?Enviado Correctamente")
    redes=iconos.objects.all()
    return render (request, "contactos/contacto.html", {'redes':redes, 'form' : contacto_formulario })