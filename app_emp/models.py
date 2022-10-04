from django.db import models

# Create your models here.


class Emp(models.Model):
    id_emp = models.AutoField(primary_key=True)
    tipo_emp = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'emp'
