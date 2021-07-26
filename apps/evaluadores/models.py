from django.db import models
from apps.parevaluador.models import Parevaluador

# Create your models here.

class Evaluadores (models.Model):
    Parevaluador = models.ForeignKey(Parevaluador, null=False, blank=False, on_delete=models.CASCADE)
    Notasfinal = models.CharField(max_length=2)
    Detallefin = models.TextField()

    def __str__(self):
        return "{} {}".format(self.Parevaluador, self.Notasfinal)