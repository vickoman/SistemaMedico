# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Cita

# Arregla toda la interfaz del modelo
class CitaAdmin(admin.ModelAdmin):

 	fieldsets = [
		('Paciente a Citar',	{'fields': ['paciente']}),
		('Detalles de la cita', {'fields': ['fecha_cita','hora_cita','pendiente']}),
	]

 	list_display = ('paciente','__unicode__')
 	list_filter = ['pendiente','fecha_cita','hora_cita']
 	search_fields = ['paciente','fecha_cita']

admin.site.register(Cita, CitaAdmin)