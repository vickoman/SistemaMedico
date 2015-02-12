# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
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
                ('edad', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
