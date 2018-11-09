from django.test import TestCase
from .models import Product


class ProductTests(TestCase):

    def test_str(self):
        '''
        Test Product Name
        '''

        test_name = Product(name='A Product')
        self.assertEqual(str(test_name), 'A Product')
