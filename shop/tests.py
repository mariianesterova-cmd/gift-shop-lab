from django.test import TestCase
from .models import Product

class ShopTest(TestCase):
    def setUp(self):
        # Створюємо пробний товар для тесту
        Product.objects.create(name="Тестовий подарунок", price=500, description="Дуже гарний")

    def test_product_content(self):
        # Перевіряємо, чи товар дійсно з'явився в базі з правильною ціною
        item = Product.objects.get(id=1)
        self.assertEqual(item.name, "Тестовий подарунок")
        self.assertEqual(item.price, 500)