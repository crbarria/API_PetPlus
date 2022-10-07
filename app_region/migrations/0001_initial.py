# Generated by Django 4.1.1 on 2022-10-07 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id_region', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_region', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'region',
                'managed': False,
            },
        ),
    ]
