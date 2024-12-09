from django.db import models


# Base Product Class
class Product(models.Model):
    name = models.CharField(max_length=255)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_price(self, quantity=1):
        """Base price calculation."""
        return self.base_price * quantity

    def __str__(self):
        return self.name


# Derived Product Classes
class SeasonalProduct(Product):
    seasonal_discount = models.DecimalField(max_digits=4, decimal_places=2, default=0.0)

    def get_price(self, quantity=1):
        """Apply seasonal discount."""
        price = super().get_price(quantity)
        return price * (1 - self.seasonal_discount)


class BulkProduct(Product):
    tiered_discounts = models.JSONField(default=dict)  # Example: {10: 0.05, 20: 0.10}

    def get_price(self, quantity):
        """Apply tiered discounts."""
        price = super().get_price(quantity)
        discount = 0
        for qty, disc in sorted(self.tiered_discounts.items(), reverse=True):
            if quantity >= qty:
                discount = disc
                break
        return price * (1 - discount)


class PremiumProduct(Product):
    markup_percentage = models.DecimalField(max_digits=4, decimal_places=2, default=0.15)

    def get_price(self, quantity=1):
        """Apply markup for premium products."""
        price = super().get_price(quantity)
        return price * (1 + self.markup_percentage)


# Base Discount Class
class Discount(models.Model):
    name = models.CharField(max_length=255)
    priority = models.IntegerField()

    def apply_discount(self, price):
        """Base discount calculation (no discount by default)."""
        return price


# Derived Discount Classes
class PercentageDiscount(Discount):
    percentage = models.DecimalField(max_digits=4, decimal_places=2)

    def apply_discount(self, price):
        """Reduce price by a percentage."""
        return price * (1 - self.percentage)


class FixedAmountDiscount(Discount):
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def apply_discount(self, price):
        """Subtract a fixed amount."""
        return max(0, price - self.amount)


class TieredDiscount(Discount):
    tiers = models.JSONField(default=dict)  # Example: {500: 0.05, 1000: 0.10}

    def apply_discount(self, price):
        """Apply discount based on tiers."""
        discount = 0
        for threshold, disc in sorted(self.tiers.items(), reverse=True):
            if price >= threshold:
                discount = disc
                break
        return price * (1 - discount)
