from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns
import uuid # Required for unique book instances

# Create your models here.
class Genero(models.Model):
	nombre_genero = models.CharField(max_length=200)
	
	def get_absolute_url(self):
		return reverse('genero-detail', args=[str(self.id)])

	def __str__(self):
		return self.nombre_genero

class Juego(models.Model):
    
	titulo = models.CharField(max_length=200)
	compañia = models.ForeignKey('Compañia', on_delete=models.SET_NULL, null=True)
    
	descirpcion = models.TextField(max_length=1000, help_text='Inserte una descripcion del juego')
	genero = models.ManyToManyField(Genero)

	def get_absolute_url(self):
		return reverse('juego-detail', args=[str(self.id)])
    
	def __str__(self):
		return self.titulo

class Compañia(models.Model):
	compañia = models.CharField(max_length=100)

	def get_absolute_url(self):
		return reverse('compañia-detail', args=[str(self.id)])

	def __str__(self):
		return self.compañia