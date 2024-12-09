from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Product, Discount, SeasonalProduct, BulkProduct, PremiumProduct
from .serializers import ProductSerializer
from decimal import Decimal

class ProductPriceView(APIView):
    def post(self, request):
        product_type = request.data.get("type")
        name = request.data.get("name")
        base_price = request.data.get("base_price")
        quantity = request.data.get("quantity", 1)

        if product_type == "seasonal":
            product = SeasonalProduct(name=name, base_price=base_price, seasonal_discount=0.2)
        elif product_type == "bulk":
            product = BulkProduct(name=name, base_price=base_price, tiered_discounts={10: 0.05, 20: 0.10})
        elif product_type == "premium":
            product = PremiumProduct(name=name, base_price=base_price, markup_percentage=0.15)
        else:
            return Response({"error": "Invalid product type"}, status=status.HTTP_400_BAD_REQUEST)

        final_price = product.get_price(quantity)
        return Response({"final_price": final_price})


class ApplyDiscountView(APIView):
    def post(self, request):
        try:
            # Get the input data
            price = Decimal(request.data.get("price", 0))
            discount_type = request.data.get("discount_type")

            # Validate price and discount type
            if not price or not discount_type:
                return Response({"error": "Price and discount_type are required"}, status=status.HTTP_400_BAD_REQUEST)

            # Apply PercentageDiscount
            if discount_type == "percentage":
                percentage = Decimal(request.data.get("percentage", 0))  # Example: 0.10 for 10%
                if percentage <= 0 or percentage > 1:
                    return Response({"error": "Invalid percentage value"}, status=status.HTTP_400_BAD_REQUEST)
                final_price = price * (1 - percentage)

            # Apply FixedAmountDiscount
            elif discount_type == "fixed":
                fixed_amount = Decimal(request.data.get("fixed_amount", 0))  # Example: 50 for $50 off
                if fixed_amount < 0:
                    return Response({"error": "Invalid fixed amount value"}, status=status.HTTP_400_BAD_REQUEST)
                final_price = max(0, price - fixed_amount)

            # Apply TieredDiscount
            elif discount_type == "tiered":
                tiers = request.data.get("tiers", {})  # Example: {"500": 0.05, "1000": 0.10}
                if not tiers or not isinstance(tiers, dict):
                    return Response({"error": "Invalid tiers value"}, status=status.HTTP_400_BAD_REQUEST)

                # Find the applicable tier
                discount = 0
                for threshold, percentage in sorted(tiers.items(), key=lambda x: Decimal(x[0]), reverse=True):
                    if price >= Decimal(threshold):
                        discount = Decimal(percentage)
                        break
                final_price = price * (1 - discount)

            # If discount type is invalid
            else:
                return Response({"error": "Invalid discount type"}, status=status.HTTP_400_BAD_REQUEST)

            # Return the calculated final price
            return Response({"final_price": round(float(final_price), 2)})

        except Exception as e:
            return Response({"error": f"Unexpected error: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    

def home(request):
    return HttpResponse("Welcome to the dynamic pricing API! Use /api/ to interact with the API.")
