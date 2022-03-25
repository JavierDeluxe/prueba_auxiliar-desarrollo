from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Usuario

class RegistroForm(UserCreationForm):
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta():
        model = Usuario
        fields = ("username", "email", "password1","password2","photo")
        labels = {"username":"Nombre completo", "email": "Correo","password1":"Ingresa la contraseña","password2":"Confirmar contraseña","photo":"Cargue foto"}

class AutheticateForm(forms.ModelForm):

    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data["email"]
        password = self.cleaned_date["password"]

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("El email o la contraseña son incorrectos")
