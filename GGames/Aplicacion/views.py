from django.shortcuts import render
from . models import Genero,Juego,Compañia
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(
        request,"index.html")

def juegos(request):
    return render(
        request,"juegos.html")

def tarjetas(request):
    return render(
        request,"tarjetas.html")

def formulario(request):
    return render(
        request,"formulario.html")
        
#compañia
class CompañiaCreate(CreateView):
    model = Compañia
    fields = '__all__'

class CompañiaUpdate(UpdateView):
    model = Compañia
    fields = ['compañia']

class CompañiaDelete(DeleteView):
    model = Compañia
    success_url = reverse_lazy('index')

class CompañiaDetailView(generic.DetailView):
    model = Compañia 

class ComapñiaListView(generic.ListView):
    model=Compañia
    paginate=10

#Genero
class GeneroCreate(CreateView):
    model= Genero
    fields='__all__'

class GeneroUpdate(UpdateView):
    model = Genero
    fields = ['nombre_genero']

class GeneroDelete(DeleteView):
    model= Genero
    success_url = reverse_lazy('index')

class GeneroDetailView(generic.DetailView):
    model=Genero

class GeneroListView(generic.ListView):
    model=Genero
    paginate=10

#Juego

class JuegoListView(generic.ListView):
    model=Juego
    paginate=10

class JuegoCreate(CreateView):
    model= Juego
    fields='__all__'

class JuegoUpdate(UpdateView):
    model = Juego
    fields = ['titulo','compañia','descirpcion','genero']

class JuegoDelete(DeleteView):
    model= Juego
    success_url = reverse_lazy('index')

class JuegoDetailView(generic.DetailView):
    model=Juego
