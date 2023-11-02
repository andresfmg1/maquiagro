"""
URL configuration for Maquiagro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include 
from core import views
from django.conf import settings
from django.conf.urls.static import static
from contactos import views as contactos_views
from portafolio import views as portafolio_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio,name='inicio'),
    path('portafolio/',portafolio_views.portafolio,name='portafolio'),
    path('carrito/',include('carrito.urls')),
    path('pedidos/',include('pedidos.urls')),
    path('productos/',views.producto,name='productos'),
    path('servicio/',views.servicio,name='servicio'),

    path('contacto/',contactos_views.contacto,name='contacto'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('Registro/',views.registro,name='registro'),

    path('cambiar-contrasena/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html'), name='password_change'),
    path('cambiar-contrasena/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
    path('restablecer-contrasena/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('restablecer-contrasena/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('restablecer-contrasena/confirmar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('restablecer-contrasena/completar/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    
    ]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)