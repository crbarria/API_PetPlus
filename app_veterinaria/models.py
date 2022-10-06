from django.db import models


# Create your models here.

class Veterinaria(models.Model):
    id_veterinaria = models.AutoField(primary_key=True)
    nombre_vet = models.CharField(max_length=45)
    direccion = models.CharField(max_length=250)
    especialidad = models.CharField(max_length=45)
    telefono = models.CharField(max_length=45)
    correo = models.CharField(max_length=45)
    urgencia = models.CharField(max_length=45, blank=True, null=True)
    exoticos = models.CharField(max_length=45, blank=True, null=True)
    odontologia = models.CharField(max_length=45, blank=True, null=True)
    toma_muestras = models.CharField(max_length=45, blank=True, null=True)
    examenes = models.CharField(max_length=45, blank=True, null=True)
    comuna_id_comuna = models.ForeignKey('app_comuna.Comuna', models.DO_NOTHING, db_column='comuna_id_comuna')

    class Meta:
        managed = False
        db_table = 'veterinaria'