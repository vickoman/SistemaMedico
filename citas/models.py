from django.db import models
import datetime

from pacientes.models import Paciente

#Modelo Citas, toda cita tiene un paciente(ForeignKey:Paciente)
class Cita(models.Model):

	paciente 	= models.ForeignKey(Paciente)
	fecha_cita	= models.DateField('Fecha de Cita')
	hora_cita	= models.TimeField('Hora de Cita')
	pendiente	= models.BooleanField(default=True)

	def __unicode__(self):
		string_cita = "Cita %s %s"%(self.fecha_cita, self.hora_cita)
		return string_cita