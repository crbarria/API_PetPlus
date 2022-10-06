# Generated by Django 4.1.1 on 2022-10-06 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dueno',
            fields=[
                ('id_dueno', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_completo', models.CharField(max_length=45)),
                ('telefono', models.IntegerField()),
                ('correo', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'dueno',
                'managed': False,
            },
        ),
    ]