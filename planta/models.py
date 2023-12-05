from django.db import models

# la definicion de los 3 modelos creados

class Docente(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    situacion_de_revista = models.CharField(max_length=20)
    sala = models.CharField(max_length=20)
    turno = models.CharField(max_length=15)
    
class Alumnx(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    fecha_nacimiento = models.DateField()
    sala = models.CharField(max_length=15)
    turno = models.CharField(max_length=15)
    
class Sala(models.Model):
    nombre = models.CharField(max_length=25)
    cantidad_alumnxs = models.IntegerField()
    turno = models.CharField(max_length=15)
    docente = models.CharField(max_length=40)