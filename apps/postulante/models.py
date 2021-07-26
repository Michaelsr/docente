from django.db import models

# Create your models here.

class Postulante (models.Model):
    Nombre = models.CharField(max_length=400)
    Apellidos = models.CharField(max_length=800)
    Correo = models.CharField(max_length=100)
    Archivo = models.FileField(upload_to="archivos/", null= True, blank= True)
    Detalle = models.TextField()
    Entrevista = models.TextField(null=True, blank=True)
    Notas = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{},{} {} {}".format(self.Apellidos, self.Nombre, self.Detalle, self.Archivo)