from django.db import models

# Create your models here.

class Curso(models.Model):   ##Le damos el formato para que lo tome como una base de datos
    nombre=models.CharField(max_length=40)  ##Aclaramos que va a ser un tipo de caracter
    camada=models.IntegerField()

def __str__(self):
    return f"Curso {self.nombre} de la camada {self.camada}"