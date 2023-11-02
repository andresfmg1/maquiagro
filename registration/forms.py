from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import ReCaptchaField



class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text=" Requerido. 254 caracteres como maximo y debe ser un email valido.")
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "captcha")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError ('El correo ya está registrado, intenta con uno nuevo.')
        return email