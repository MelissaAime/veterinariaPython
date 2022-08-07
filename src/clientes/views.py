from django.shortcuts import render
from django.http import HttpResponse
from clientes.models import Cliente, Mascotas, Veterinario

def inicio(request):
    return render(request, "clientes/index.html")

def cliente(request):
    clientes = Cliente.objects.all()

    context = {"clientes" : clientes}

    return render(request, "clientes/clientes.html", context)

def mascotas(request):
    mascotas = Mascotas.objects.all()

    context = {"mascotas" : mascotas}

    return render(request, "clientes/mascotas.html", context)

def veterinarios(request):
    veterinarios = Veterinario.objects.all()

    context = {"veterinarios" : veterinarios}
    return render(request, "clientes/veterinarios.html", context)
