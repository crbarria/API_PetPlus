# Generated by Django 4.1.1 on 2022-10-10 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id_animal', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('n_microchip', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'animal',
                'managed': False,
            },
        ),
    ]
