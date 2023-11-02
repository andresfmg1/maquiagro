from .forms import UserCreationFormWithEmail
#from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from core.models import iconos
from django.shortcuts import render
from captcha.fields import ReCaptchaField

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'
    
    def get_success_url(self):
        return reverse_lazy('login') + '?register'
    

def get_form(self, request, form_class=None) :
        form=super(SignUpView,self).get_form()

        form.fields['username'].widget=forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre del usuario'})
        form.fields['email'].widget=forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Correo@valido.com'})
        form.fields['password1'].widget=forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget=forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Confirmar Contraseña'})
        
        form.fields['username'].label='' # ocultar los label
        form.fields['password1'].label=''
        form.fields['password2'].label=''
        return form
