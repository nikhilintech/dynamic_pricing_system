from django.urls import path
from .views import ProductPriceView, ApplyDiscountView

urlpatterns = [
    path('product-price/', ProductPriceView.as_view(), name='product_price'),
    path('apply-discount/', ApplyDiscountView.as_view(), name='apply_discount'),
]
