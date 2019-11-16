from django.db import models
from habitacion.models import habitacion

# Create your models here.
class empresaDatos(models.Model):
    rutEmpresa = models.CharField(max_length=70)
    nombreEmpresa = models.CharField(max_length=70)
    giroEmpresa = models.CharField(max_length=70)
    dirEmpresa = models.CharField(max_length=150)
    userEmpresa = models.CharField(max_length=100)
    passEmpresa = models.CharField(max_length=50)

class comedorDatos(models.Model):
# Se debe registrar los diferentes platos que entrega como servicio de comedor con sus respectivos precios. 
# Estos platos deben estar orientado a: Servicios ejecutivos, Especiales, Generales, etc., con una minuta semanal. m

    tipoPlato = models.CharField(max_length=70)
    entrada = models.CharField(max_length=70)
    platoFondo = models.CharField(max_length=70)
    postre = models.CharField(max_length=70)
    valorMenu = models.IntegerField()

    def __str__(self):
        return self.tipoPlato

class facturaDatos(models.Model):
    rut_Emp_Fac = models.CharField(max_length=70)
    nombre_Emp_Fac = models.CharField(max_length=70)
    giro_Emp_Fac = models.CharField(max_length=70)
    dir_Emp_Fac = models.CharField(max_length=70)
    tipo_Serv_Fac = models.ForeignKey(comedorDatos, on_delete=models.CASCADE, blank=True, null=False)
    valor_Serv_Fac = models.IntegerField()
    tipo_Hab_Fac = models.ForeignKey(habitacion, on_delete=models.CASCADE, blank=True, null=False)
    valor_Hab_Fac = models.IntegerField()
    total_Fac = models.IntegerField()

