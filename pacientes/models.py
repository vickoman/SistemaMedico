from django.db import models

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
	edad 		= models.IntegerField()

	#Concatena y devuelve el nombre con apellidos, use __str__ in Python 3.4.x
	def __unicode__(self):
		nombreCompleto = "%s %s"%(self.nombre, self.apellidos)
		return nombreCompleto