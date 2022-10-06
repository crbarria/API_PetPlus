from django.db import models

# Create your models here.

class Procedimiento(models.Model):
    id_procedimiento = models.AutoField(primary_key=True)
    nombre_procedimiento = models.CharField(max_length=45)
    dias = models.CharField(max_length=45)
    dosis = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'procedimiento'