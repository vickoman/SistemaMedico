# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Paciente
from citas.models import Cita

# Agrega citas debajo del modelo Paciente en la interfaz del Admin
class CitaEnLinea(admin.TabularInline):
 	model 	= Cita
 	extra	= 3

# Arregla como se va a ver el modelo Paciente en la interfaz del Admin
class PacienteAdmin(admin.ModelAdmin):

	fieldsets = [
		('Datos de Contacto',	{'fields': ['cedula','nombre','apellidos','edad','telefono','direccion']}),
		('Detalles del Paciente', {'fields': ['medicamento','enfermedad','alergia','observacion']}),
	]

 	inlines = [CitaEnLinea]

 	list_display = ('__unicode__','telefono')
 	list_filter = ['alergia']
 	search_fields = ['nombre','apellidos']

admin.site.register(Paciente, PacienteAdmin)