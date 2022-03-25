from pyexpat.errors import messages
from unicodedata import name
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import AutheticateForm, RegistroForm

def index(request):
    return render(request, "article/index.html",{})

def registro(request):
    form = RegistroForm()
    return render(request, "article/registro.html",{"form":form})

def iniciar_sesion(request):
    form = AutheticateForm()
    return render(request, "article/iniciar_sesion.html",{"form":form})

def cerrar_sesion(request):
    logout(request)
    messages.info(request, "Saliste de la pagina")
    return redirect("article/index.html")

def ver_articulo(request):
    return render(request, "article/ver_articulo.html", {})

def crear_articulo(request):
    return render(request, "article/crear_articulo.html",{})

def registro_exitoso(request):
        name_post = request.POST['name']
        password_post = request.POST['password']
        email_post = request.POST['correo']
        image_post = request.POST.get('imagen',False)
        nuevo_objeto = User(name=name_post, photo=image_post, email=email_post,password=password_post)
        nuevo_objeto.save()
        return render(request, "article/registro_exitoso.html",{"name":name_post,"password":password_post,"correo":email_post,"image":image_post})