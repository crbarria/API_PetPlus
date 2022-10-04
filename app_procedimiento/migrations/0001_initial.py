# Generated by Django 4.1.1 on 2022-10-04 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Procedimiento',
            fields=[
                ('id_procedimiento', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_procedimiento', models.CharField(max_length=45)),
                ('dias', models.CharField(max_length=45)),
                ('dosis', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'procedimiento',
                'managed': False,
            },
        ),
    ]
