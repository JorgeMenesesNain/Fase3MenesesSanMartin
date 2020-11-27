from django.contrib import admin

# Register your models here.
from . models import Genero, Juego, Compañia

admin.site.register(Genero)
admin.site.register(Juego)
admin.site.register(Compañia)