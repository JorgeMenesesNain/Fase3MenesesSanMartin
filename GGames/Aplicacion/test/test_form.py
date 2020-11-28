from django.test import TestCase
from Aplicacion.forms import CompañiaForm
from Aplicacion.models import Compañia


class CompañiaFormsTest(TestCase):
    def test_valid_form(self):
        c = Compañia.objects.create(compañia='activishion')
        data = {'compañia': c.compañia,}
        form = CompañiaForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        c = Compañia.objects.create(compañia='',)
        data = {'compañia': c.compañia,}
        form = CompañiaForm(data=data)
        self.assertFalse(form.is_valid())