from django.db import models
from apps.postulante.models import Postulante

# Create your models here.

class Comision (models.Model):
    Postulante = models.ForeignKey(Postulante, null=False, blank=False, on_delete=models.CASCADE)
    Entrevista = models.CharField(max_length=6)
    Nota= models.CharField(max_length=2)
    Detalles= models.TextField()

    def __str__(self):
        return "{}, #{} N{}".format(self.Postulante.Nombre, self.Entrevista, self.Nota)