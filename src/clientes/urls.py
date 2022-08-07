from django.urls import path
from clientes.views import *

urlpatterns = [
    path("", inicio, name="inicio"),
    path("clientes/", cliente, name="clientes"),
    path("mascotas/", mascotas, name="mascotas"),
    path("veterinarios/", veterinarios, name="veterinarios")
]