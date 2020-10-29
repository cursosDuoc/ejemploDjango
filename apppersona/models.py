from django.db import models
from .validadores_chilenos import validate_chilean_rut

# Create your models here.
class Persona(models.Model):
    nombre = models.TextField(max_length=30)
    apellido = models.TextField(max_length=30)
    rut = models.TextField(max_length=15, validators=[validate_chilean_rut])

    def __str__(self) :
        return self.nombre + " " + self.apellido


class TarjetaJunaeb(models.Model):
    # Los identificadores, aunque sea digitos, no son numeros.
    numeroTarjeta = models.TextField(max_length=12) # es un identificador
    montoDisponible = models.IntegerField()
    rut = models.TextField(max_length=15 , validators=[validate_chilean_rut])
    clave = models.TextField(max_length=8)

    def __str__(self) :
        return self.rut + " " + self.numeroTarjeta
