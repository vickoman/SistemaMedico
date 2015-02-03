# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_cita', models.DateField(verbose_name=b'Fecha de Cita')),
                ('hora_cita', models.TimeField(verbose_name=b'Hora de Cita')),
                ('pendiente', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cedula', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('telefono', models.IntegerField()),
                ('direccion', models.TextField()),
                ('medicamento', models.CharField(max_length=200)),
                ('enfermedad', models.CharField(max_length=200)),
                ('alergia', models.BooleanField(default=False)),
                ('observacion', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cita',
            name='paciente',
            field=models.ForeignKey(to='citas_pacientes.Paciente'),
            preserve_default=True,
        ),
    ]
