from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    telefono = models.IntegerField()

    def __str__(self):
        return f"Cliente {self.id}: {self.nombre}"

class Mascotas(models.Model):
    nombre = models.CharField(max_length=40)
    raza = models.CharField(max_length=40)
    fecha_nac = models.DateField()

    def __str__(self):
        return f"Mascota {self.nombre} - {self.raza}"

class Veterinario(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    matricula = models.IntegerField()

    def __str__(self):
        return f"Veterinario: {self.nombre} {self.apellido} - {self.matricula}"
