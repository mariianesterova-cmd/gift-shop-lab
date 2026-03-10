from django.test import TestCase
from .models import Product

class ShopTest(TestCase):
    def test_basic_math(self):
        # Це найпростіший тест у світі, щоб просто перевірити, чи працює CI
        self.assertEqual(1 + 1, 2)

    def test_create_product(self):
        # Перевіряємо створення продукту
        Product.objects.create(name="Подарунок", price=100)
        self.assertEqual(Product.objects.count(), 1)