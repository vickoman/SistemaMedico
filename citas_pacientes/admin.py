# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Paciente, Cita

# Agrega citas debajo del modelo Paciente en la interfaz del Admin
class CitaEnLinea(admin.StackedInline):
 	model 	= Cita
 	extra	= 3

# Arregla como se va a ver el modelo Paciente en la interfaz del Admin
class PacienteAdmin(admin.ModelAdmin):

	fieldsets = [
		('Datos de Contacto',	{'fields': ['cedula','nombre','apellidos','telefono','direccion']}),
		('Detalles del Paciente', {'fields': ['medicamento','enfermedad','alergia','observacion']}),
	]

 	inlines = [CitaEnLinea]

 	list_display = ('__unicode__','telefono')
 	list_filter = ['alergia']
 	search_fields = ['nombre','apellidos']

# Arregla toda la interfaz del modelo
class CitaAdmin(admin.ModelAdmin):

 	fieldsets = [
		('Paciente a Citar',	{'fields': ['paciente']}),
		('Detalles de la cita', {'fields': ['fecha_cita','hora_cita','pendiente']}),
	]

 	list_display = ('paciente','__unicode__')
 	list_filter = ['pendiente','fecha_cita','hora_cita']
 	search_fields = ['paciente','fecha_cita']

admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Cita, CitaAdmin)