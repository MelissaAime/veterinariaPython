from django.forms import Form, CharField, IntegerField

#Buscar veterinario:
class FormBuscarVeterinario(Form):
    nombre_veterinario = CharField(max_length=100) 

#Buscar mascota:
class FormBuscarMascota(Form):
    nombre_mascota = CharField(max_length=100) 

#Crear cliente:
class FormClienteCrear(Form):
    nombre = CharField(max_length=40)
    apellido = CharField(max_length=40)
    telefono = IntegerField()
