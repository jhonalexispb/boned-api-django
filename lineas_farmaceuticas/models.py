from django.db import models

class LineasFarmaceuticas(models.Model):
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=20)
    fecha_cracion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
