from django.db import models

# Create your models here.

class Dueno(models.Model):
    id_dueno = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=45)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dueno'
