from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.db import connection
from thumbs import ImageWithThumbsField
# Create your models here.
class jugador (models.Model):
	nombre=models.CharField(max_length=200)
	apellidos=models.CharField(max_length=200)
	direccion=models.CharField(max_length=200)
	telefono=models.IntegerField()
	email=models.EmailField(max_length=75)
	ci=models.IntegerField(unique=True)
	fecha=models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return "%s "%(self.nombre)

class Perfil(models.Model):	
	user=models.OneToOneField(User,unique=True)
	pais=models.CharField(max_length="30", null=False)
	avatar=ImageWithThumbsField(upload_to="img_user",sizes=((50,50),(200,200)))




class Tema(models.Model):
	nombre=models.CharField(max_length=20,unique=True)
	def __str__(self):
		return self.nombre

class Pregunta(models.Model):
	nombre=models.CharField(max_length=500)
	tema=models.ForeignKey(Tema)
	def __str__(self):
		return self.nombre


class Respuesta(models.Model):
	respuesta_correcta=models.CharField(max_length=500)
	respuesta_opcional=models.CharField(max_length=500)
	respuesta_opcional_1=models.CharField(max_length=500)
	respuesta_opcional_2=models.CharField(max_length=500)
	pregunta=models.ForeignKey(Pregunta)
	def __str__(self):
		return self.pregunta


	