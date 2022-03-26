from cmath import phase
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
    data = {
        'form' : RegistroForm()
    }
    print("paso 1")
    if request.method == 'POST':
        print("paso 2")
        formulario = RegistroForm(request.POST)
        if formulario.is_valid():
            user_save = formulario.save()
            username1 = formulario.cleaned_data["username"]
            password1 = formulario.cleaned_data["password1"]
            user = UserProfile(user=user_save, photo=request.POST.get('photo'))
            user.save()
            user = authenticate(username=username1, password=password1)
            login(request, user)
            return redirect(request, "article/index.html")
        data['form'] = formulario

    return render(request, "article/registro.html",data)

def iniciar_sesion(request):
    if request.method == 'POST':
        username1 = request.POST.get['username']
        password1 = request.POST.get['password']
        usuario = authenticate(username=username1, password = password1)
        login(usuario,password1)
    return render(request, "article/iniciar_sesion.html")

def cerrar_sesion(request):
    logout(request)
    return render("index.html")

def ver_articulo(request):
    return render(request, "article/ver_articulo.html", {})

def crear_articulo(request):
    return render(request, "article/crear_articulo.html",{})

def registro_exitoso(request):
    print("paso 3")
    #print(request)
    #data = request.POST["form"]
    #name_post = "hi"
    #password_post = r"2"
    #email_post = "3"
    #image_post = "5"
    #nuevo_objeto = Usuario(username=name_post, photo=image_post, email=email_post,password=password_post)
    #nuevo_objeto.save()
    #return render(request, "article/registro_exitoso.html",{"name":name_post,"password":password_post,"correo":email_post,"image":image_post})
    return render(request, "article/registro_exitoso.html",{})