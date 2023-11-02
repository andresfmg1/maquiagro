from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from pedidos.forms import UserProfileForm
from pedidos.models import UserProfile
from pedidos.models import Pedido, LineaPedido
from carrito.carrito import carrito
from carrito.context_processor import importe_total_carro
from portafolio.models import project
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags
from core.models import iconos

# Create your views here.

@login_required(login_url="/registration/signup")   #Este decorador garantiza que la vista procesar_pedido solo pueda ser accedida por usuarios autenticados
def procesar_pedido(request):
    user_profile = UserProfile.objects.filter(user=request.user).first()  #Recupera el perfil del usuario asociado al usuario que ha iniciado sesión.
    if request.method == 'POST':
        user_profile_form = UserProfileForm(request.POST)   #Valida los datos del formulario utilizando UserProfileForm.
        if user_profile_form.is_valid():
            if not user_profile:                                     #Si el usuario no tiene un perfil de usuario
                user_profile = user_profile_form.save(commit=False)  #crea uno nuevo y lo asocia al usuario.
                user_profile.user = request.user
            else:
                user_profile_form = UserProfileForm(request.POST, instance=user_profile)  # Actualiza el perfil existente
            user_profile_form.save()

            pedido=Pedido.objects.create(user=request.user)  #Crea un nuevo objeto Pedido asociado al usuario.
            carro=carrito(request)     #Recupera el carrito de compras del usuario (carro) y procesa su contenido para crear objetos LineaPedido.
            lineas_pedido=list()       #variable en donde se almacenara los items del carro
            for key, value in carro.carrito.items():  #Por cada clave valor que haya en los items del carro
                lineas_pedido.append(LineaPedido(   ## se rescata la informacion que interesa 
                    producto_id=key,
                    cantidad=value["cantidad"],            
                    user=request.user,
                    pedido=pedido
                    ))

            LineaPedido.objects.bulk_create(lineas_pedido)     # se almacena la lista lineas_pedido en la base de datos

            precio_total = sum(linea.producto.price * linea.cantidad for linea in lineas_pedido)

            enviar_mail(                #Llama a la función enviar_mail para enviar una notificación por correo electrónico con los detalles del pedido.
                pedido=pedido,
                lineas_pedido=lineas_pedido,
                nombreusuario=request.user.username,            
                emailusuario=request.user.email,
                user_profile_form= user_profile_form,
                precio_total=precio_total 
            )

            messages.success(request,"El pedido se ha creado correctamente")

            return redirect("../portafolio")
    else:
        user_profile_form = UserProfileForm()     # Si la solicitud no es POST, crea una instancia de UserProfileForm vacía.

    return render(request, 'emails/formulario.html', {'user_profile_form': user_profile_form})

def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("emails/pedido.html",{
        "pedido": kwargs.get("pedido"),
        "lineas_pedido":kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreusuario"),
        "emailusuario":kwargs.get("emailusuario"),
        "precio_total":kwargs.get("precio_total"),
        "user_profile_form":kwargs.get("user_profile_form")
        })

    mensaje_texto=strip_tags(mensaje) ##variable que es igual a la otra variable de mensaje pero ingnorando las etiquetas html de la ubucacion del archivo
    from_email="vdmartinez65@misena.edu.co"
    to=kwargs.get("emailusuario")
    #to="victordanielmar91@gmail.com"
    send_mail(asunto,mensaje_texto,from_email,[to], html_message=mensaje)
        
def portafolio(request):
    redes=iconos.objects.all()
    projects=project.objects.all()
    return  render(request,"pedidos/formulario.html",{'projects':projects,'redes':redes})
