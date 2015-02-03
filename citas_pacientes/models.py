from django.db import models
import datetime

#Modelo Paciente
class Paciente(models.Model):

	cedula		= models.IntegerField(unique=True)
	nombre		= models.CharField(max_length=200)
	apellidos	= models.CharField(max_length=200)
	telefono	= models.IntegerField()
	direccion	= models.TextField()
	medicamento = models.CharField(max_length=200)
	enfermedad	= models.CharField(max_length=200)
	alergia		= models.BooleanField(default=False)
	observacion = models.TextField()

	#Concatena y devuelve el nombre con apellidos, using __str__ in Python 3.4.x
	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.nombre, self.apellidos)
		return nombreCompleto

#Modelo Citas, toda cita tiene un paciente(ForeignKey:Paciente)
class Cita(models.Model):

	paciente 	= models.ForeignKey(Paciente)
	fecha_cita	= models.DateField('Fecha de Cita')
	hora_cita	= models.TimeField('Hora de Cita')
	pendiente	= models.BooleanField(default=True)

	def __unicode__(self):
		string_cita = "Cita %s %s"%(self.fecha_cita, self.hora_cita)
		return string_cita