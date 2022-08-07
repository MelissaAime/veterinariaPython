from django.shortcuts import render
from django.http import HttpResponse
from clientes.models import Cliente, Mascotas, Veterinario
from clientes.forms import FormBuscar, FormClienteCrear

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

    lista_veterinarios = Veterinario.objects.all()
    
    #Formulario de búsqueda:
    if request.GET.get("nombre_veterinario"):

        formularioVete = FormBuscar(request.GET)

        if formularioVete.is_valid():
            data = formularioVete.cleaned_data
            lista_veterinarios = Veterinario.objects.filter(nombre__icontains = data['nombre_veterinario'])
        
        return render(request, "clientes/veterinarios.html", {"veterinarios": lista_veterinarios, "formularioVete": formularioVete})
    
    else:
        formularioVete = FormBuscar()
        return render(request, "clientes/veterinarios.html", {"veterinarios": lista_veterinarios, "formularioVete": formularioVete})


def cliente_nuevo(request):
    return render(request, "clientes/cliente_nuevo.html")


def crear_cliente(request):

    if request.method == "GET":
        formulario = FormClienteCrear()
        return render(request,"clientes/clientes.html", {"formulario": formulario})

    else:

        formulario = FormClienteCrear(request.POST)

        if formulario.is_valid():
            
            data = formulario.cleaned_data

            nombre = data.get['nombre']
            apellido = data.get['apellido']
            telefono = data.get['telefono']

            cliente = Cliente(nombre=nombre, apellido=apellido, telefono=telefono)
            cliente.save()

            return render(request, "clientes/clientes.html")

        else:
            return HttpResponse("Formulario no valido")