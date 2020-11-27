from django.test import TestCase
from Aplicacion.models import Compañia,Genero,Juego

class JuegoTestCase(TestCase):
    def setUp(self):
        Compañia.objects.create(compañia='Activisiom')

    def test_compañia_juego(self):
        compañia1 = Compañia.objects.get(compañia='Activisiom')
        self.assertEqual(compañia1.compañia, 'Activisiom')