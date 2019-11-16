from django.db import models

# Create your models here.

class tipoCama(models.Model):
    descCama = models.CharField(max_length=70)
    def __str__(self):
        return self.descCama

class estadoHab(models.Model):
    descEstado = models.CharField(max_length=70)
    def __str__(self):
        return self.descEstado

class habitacion(models.Model):
    nroHabitacion = models.IntegerField(null=False)
    tipoHabitacion = models.CharField(max_length=70, null=True)
    tipoCama = models.ForeignKey(tipoCama, on_delete=models.CASCADE, blank=True, null=False)
    accesorios = models.CharField(max_length=70, null=True)
    precio = models.IntegerField(null=False)
    estado_habitacion = models.ForeignKey(estadoHab, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.tipoHabitacion
