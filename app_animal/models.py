from django.db import models

# Create your models here.

class Animal(models.Model):
    id_animal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)      
    sexo = models.CharField(max_length=45)        
    especie = models.CharField(max_length=45)     
    altura = models.CharField(max_length=45, blank=True, null=True)
    color = models.CharField(max_length=45, blank=True, null=True)
    n_microchip = models.CharField(max_length=45, blank=True, null=True)
    raza = models.CharField(max_length=45, blank=True, null=True)
    dueno_id_dueno = models.ForeignKey('app_dueno.Dueno', models.DO_NOTHING, db_column='dueno_id_dueno')
    ficha_veterinaria_id_ficha = models.ForeignKey('app_ficha.FichaVeterinaria', models.DO_NOTHING, db_column='ficha_veterinaria_id_ficha')

    class Meta:
        managed = False
        db_table = 'animal'
