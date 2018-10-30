from django.test import TestCase


class TestTreatmentViews(TestCase):
    ''' test the treatments view '''

    def test_treatments_view(self):
        # direct to the treatments view
        page = self.client.get('/')
        # check if it has a status code 200
        self.assertEqual(page.status_code, 200)
        # check that you are directed to the treatments.html page
        self.assertTemplateUsed(page, "index.html")
