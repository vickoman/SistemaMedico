# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_cita', models.DateField(verbose_name=b'Fecha de Cita')),
                ('hora_cita', models.TimeField(verbose_name=b'Hora de Cita')),
                ('pendiente', models.BooleanField(default=True)),
                ('paciente', models.ForeignKey(to='pacientes.Paciente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
