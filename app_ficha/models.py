from django.db import models

# Create your models here.

class FichaVeterinaria(models.Model):
    id_ficha = models.AutoField(primary_key=True)
    n_registro = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ficha_veterinaria'

    def __str__(self):
        return f'{self.n_registro}'

