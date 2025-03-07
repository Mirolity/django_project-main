from django.test import TestCase
from .models import Category, Product


class CatalogTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Test Category', description='Test Description')
        self.product = Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=99.99,
            category=self.category
        )

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Test Category')

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Test Product')
