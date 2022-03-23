from django.contrib import admin
from django.urls import path
from . import views

app_name = "article"

urlpatterns = [
    path("",views.index,name = "index"),
    path("registro/",views.registro, name="registro"),
    path("iniciar_sesion/", views.iniciar_sesion, name="iniciar_sesion"),
    path("ver_articulo/", views.ver_articulo, name="ver_articulo"),
    path("crear_articulo/", views.crear_articulo, name="crear_articulo"),
    path("registro_exitoso", views.registro_exitoso, name="registro_exitoso"),
]


