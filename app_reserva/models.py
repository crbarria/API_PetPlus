from django.db import models
from app_veterinaria.models import *
# Create your models here.

class ReservaHoras(models.Model):
    id_reserva_horas = models.AutoField(primary_key=True)
    horas = models.CharField(max_length=45)
    veterinaria_id_veterinaria = models.ForeignKey('app_veterinaria.Veterinaria', models.DO_NOTHING, db_column='veterinaria_id_veterinaria')
    # estado_hora_id_estado_hora = models.ForeignKey('app_estado_hora.Estado', models.DO_NOTHING, db_column='estado_hora_id_estado_hora')

    class Meta:
        managed = False
        db_table = 'reserva_horas'

    # def __str__(self):
    #     return f'{self.horas}|{self.veterinaria_id_veterinaria}|{self.estado_hora_id_estado_hora}'    

