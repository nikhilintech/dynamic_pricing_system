from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from django.http import HttpResponse
from decimal import Decimal

class BulkDiscountView(APIView):
    def post(self, request):
        try:
            data = request.data
            product_id = data.get('product_id')
            quantity = data.get('quantity')

            if not product_id or not quantity:
                return Response({'error': 'product_id and quantity are required'}, status=status.HTTP_400_BAD_REQUEST)

            # Get the product by its ID
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

            # Ensure base_price and quantity are Decimals for accurate calculations
            base_price = Decimal(product.base_price)
            quantity = Decimal(quantity)

            # Calculate discount based on quantity
            if 10 <= quantity <= 20:
                discount = Decimal(0.05)
            elif 21 <= quantity <= 50:
                discount = Decimal(0.10)
            elif quantity > 50:
                discount = Decimal(0.15)
            else:
                discount = Decimal(0.0)

            # Calculate the total base price for the given quantity
            total_base_price = base_price * quantity

            # Final price after discount
            final_price = total_base_price * (Decimal(1) - discount)

            # Prepare response data, rounding to two decimal places for price values
            return Response({
                'product': product.name,
                'quantity': int(quantity),
                'base_price': round(float(total_base_price), 2),  # Correct base price for total quantity
                'discount': f"{int(discount * 100)}%",  # Discount as a percentage
                'final_price': round(float(final_price), 2)  # Correct final price after discount
            })
        except Exception as e:
            return Response({'error': f"Unexpected error: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

class OrderDiscountView(APIView):
    def post(self, request):
        try:
            # Print the incoming data to debug
            print(f"Received request data: {request.data}")
            
            items = request.data.get('items', [])
            
            if not items:
                return Response({'error': 'Items are required'}, status=status.HTTP_400_BAD_REQUEST)

            total_price = Decimal(0)  # Initialize total price as Decimal for accuracy
            for item in items:
                if not isinstance(item, dict):
                    return Response({'error': 'Each item should be a dictionary with product_id and quantity'}, status=status.HTTP_400_BAD_REQUEST)
                
                product_id = item.get('product_id')
                quantity = item.get('quantity')

                # Ensure product_id and quantity exist
                if not product_id or not quantity:
                    return Response({'error': 'Each item must have a product_id and quantity'}, status=status.HTTP_400_BAD_REQUEST)

                # Get the product by its ID
                try:
                    product = Product.objects.get(id=product_id)
                except Product.DoesNotExist:
                    return Response({'error': f'Product with id {product_id} not found'}, status=status.HTTP_404_NOT_FOUND)

                total_price += Decimal(product.base_price) * Decimal(quantity)

            # Calculate discount based on total price
            if 500 <= total_price <= 1000:
                discount = Decimal(0.05)
            elif total_price > 1000:
                discount = Decimal(0.10)
            else:
                discount = Decimal(0.0)

            final_total = total_price * (Decimal(1) - discount)

            # Prepare response data
            return Response({
                'total_price': round(float(total_price), 2),
                'discount': f"{int(discount * 100)}%",
                'final_total': round(float(final_total), 2)
            })
        except Exception as e:
            return Response({'error': f"Unexpected error: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

def home(request):
    return HttpResponse("Welcome to the dynamic pricing API! Use /api/ to interact with the API.")
