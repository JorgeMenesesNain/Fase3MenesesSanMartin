from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('juegos/',views.juegos,name='juegos'),
    path('tarjetas/',views.tarjetas,name='tarJetas'),
    path('formulario/',views.formulario,name='formulario'),
    path('ju/',views.JuegoListView.as_view(),name='ju'),
    path('j/<int:pk>',views.JuegoDetailView.as_view(),name='juego-detail'),
    path('compañia/<int:pk>',views.CompañiaDetailView.as_view(), name='compañia-detail'),
    path('genero/<int:pk>',views.GeneroDetailView.as_view(), name='genero-detail'),
]

urlpatterns+= [
    path('compañia/create/',views.CompañiaCreate.as_view(), name='compañia_create'),
    path('compañia/<int:pk>/delete/',views.CompañiaDelete.as_view(), name='compañia_delete'),
    path('compañia/<int:pk>/update/',views.CompañiaUpdate.as_view(), name='compañia_update'),

    path('j/create/',views.JuegoCreate.as_view(), name='juego_create'),
    path('j/<int:pk>/delete/',views.JuegoDelete.as_view(), name='juego_delete'),
    path('J/<int:pk>/update/',views.JuegoUpdate.as_view(), name='juego_update'),

    path('genero/create/',views.GeneroCreate.as_view(), name='genero_create'),
    path('genero/<int:pk>/delete/',views.GeneroDelete.as_view(), name='genero_delete'),
    path('genero/<int:pk>/update/',views.GeneroUpdate.as_view(), name='genero_update'),
]