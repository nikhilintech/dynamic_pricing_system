from django.test import TestCase
from .models import Product

class DiscountAPITestCase(TestCase):
    def setUp(self):
        # Create three products
        self.product1 = Product.objects.create(name="T-shirt", base_price=10.0)
        self.product2 = Product.objects.create(name="Laptop", base_price=600.0)
        self.product3 = Product.objects.create(name="Monitor", base_price=400.0)

    def test_bulk_discount(self):
        response = self.client.post('/api/bulk-discount/', {
            'product_id': self.product1.id,
            'quantity': 25
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['final_price'], 225.0)

    def test_order_discount(self):
        # Correct data structure: items should be a list of dictionaries
        data = {
            "items": [
                {"product_id": self.product1.id, "quantity": 60},  # 60 T-shirts
                {"product_id": self.product2.id, "quantity": 5}    # 5 Laptops
            ]
        }

        response = self.client.post('/api/order-discount/', data, content_type='application/json')

        print(f"Response status: {response.status_code}")
        print(f"Response data: {response.data}")

        self.assertEqual(response.status_code, 200)

        # Calculate the expected final total:
        # Product 1 (T-shirt): 60 * $10 = $600
        # Product 2 (Laptop): 5 * $600 = $3000
        # Total = $600 + $3000 = $3600
        # Discount (since total is > $1000): 10%
        # Final total = $3600 * 0.90 = $3240

        self.assertEqual(response.data['final_total'], 3240.0)