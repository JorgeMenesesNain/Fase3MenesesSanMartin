from django.test import TestCase
from django.urls import reverse


from Aplicacion.models import Compañia

class CompañiaListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #Create 10 authors for pagination tests
        number_of_compañia = 10
        for compañia_id in range(number_of_compañia):
            Compañia.objects.create(
                compañia=f' Activishion{compañia_id}',
            )

    def test_view_url_exists_at_desired_location(self): 
        resp = self.client.get('/Aplicacion/compañia/') 
        self.assertEqual(resp.status_code, 200)  
           
    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('compañia'))
        self.assertEqual(resp.status_code, 200)
        
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('compañia'))
        self.assertEqual(resp.status_code, 200)

        self.assertTemplateUsed(resp, 'Aplicacion/compañia_list.html')
        
   