from cgitb import text
from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(attrs={'placeholder':'Escriba su nombre','class':'form-control' }), min_length=3, max_length=100)
    correo = forms.EmailField(label="Correo electeronico", required=True, widget=forms.EmailInput(attrs={'placeholder':'Escriba su correo','class':'form-control' }), min_length=3, max_length=100)
    contenido = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(attrs={'class':'form-control','rows':3 }))