from django.db import models

# Create your models here.


class Emp(models.Model):
    id_emp = models.AutoField(primary_key=True)
    nombre_empleado = models.CharField(max_length=45)
    tipo_emp = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'emp'

    def __str__(self):
        return f'{self.nombre_empleado} | {self.tipo_emp}'