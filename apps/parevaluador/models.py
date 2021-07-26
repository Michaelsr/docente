from django.db import models
from apps.comision.models import Comision

# Create your models here.

class Parevaluador (models.Model):
    Comision = models.ForeignKey(Comision, null=False, blank=False, on_delete=models.CASCADE)
    Detalle = models.TextField()
    Pareva = models.CharField(max_length=6)
    Nota = models.CharField(max_length=2)

    def __str__(self):
        return "{} {} {} {}".format(self.Comision, self.Detalle, self.Pareva, self.Nota)