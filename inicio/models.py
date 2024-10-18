from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    propietario = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.raza})"
