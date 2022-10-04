from django.db import models
from app_veterinaria.models import *
# Create your models here.

class ReservaHoras(models.Model):
    id_reserva_horas = models.AutoField(primary_key=True)
    horas = models.CharField(max_length=45)
    veterinaria_id_veterinaria = models.ForeignKey('app_veterinaria.Veterinaria', models.DO_NOTHING, db_column='veterinaria_id_veterinaria')

    class Meta:
        managed = False
        
        
        db_table = 'reserva_horas'

