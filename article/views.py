from cmath import phase
from pyexpat.errors import messages
from unicodedata import name
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from django.contrib.auth import login, logout, authenticate
from .forms import RegistroForm
from datetime import datetime

def index(request):
    articulos = Article.objects.all()
    return render(request, "article/index.html",{"articles":articulos})

def registro(request):
    data = {
        'form' : RegistroForm()
    }
    if request.method == 'POST':
        formulario = RegistroForm(request.POST)
        if formulario.is_valid():
            user_save = formulario.save()
            username1 = formulario.cleaned_data["username"]
            password1 = formulario.cleaned_data["password1"]
            user = UserProfile(user=user_save, photo=request.POST.get('photo'))
            user.save()
            user = authenticate(username=username1, password=password1)
            login(request, user)
            return redirect("/")
        data['form'] = formulario

    return render(request, "article/registro.html",data)

def iniciar_sesion(request):
    if request.method == 'POST':
        username1 = request.POST.get('username')
        password1 = request.POST.get('password')
        usuario = authenticate(username=username1, password = password1)
        if usuario is not None:
            login(request, usuario)
            return redirect("/")
        
    return render(request, "article/iniciar_sesion.html")

def cerrar_sesion(request):
    logout(request)
    return redirect("/")

def ver_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    comentarios = Comment.objects.filter(publicacion_fk_id=id)
    if request.method == 'POST':
        author = articulo.author_fk
        texto = request.POST.get('texto')
        comentario = Comment(author_fk=author,text =texto,publicacion_fk=articulo)
        comentario.save()
        redirect("article/ver_articulo.html",{"articulo":articulo})
    return render(request, "article/ver_articulo.html", {"articulo":articulo,"comentarios":comentarios})



def crear_articulo(request):
    id_usuario = request.session['_auth_user_id']
    if request.method == 'POST':
        titulo = request.POST.get("titulo")
        texto = request.POST.get('texto')
        foto = request.POST.get('foto')
        author = UserProfile.objects.get(user_id=id_usuario)
        fecha = datetime.now()
        art = Article(title=titulo,author_fk=author,text=texto,image=foto,date=fecha)
        art.save()
        comment = Comment(author_fk=author, text="Comentario necesario",publicacion_fk=art)
        comment.save()
        second_comment = Comment_second_level(author_fk=author, text="Comentario necesario",comentario_fk=comment)
        second_comment.save()
        return redirect("/")
    return render(request, "article/crear_articulo.html",{})

def registro_exitoso(request):
    return render(request, "article/registro_exitoso.html",{})

def dar_heart(request, id):
    user = request.user.id
    print(user)
    seleccionado = get_object_or_404(Article, pk=id)
    seleccionado.hearts = seleccionado.hearts+1
    seleccionado.save()
    return redirect("/")