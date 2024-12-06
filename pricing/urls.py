from django.urls import path
from .views import BulkDiscountView, OrderDiscountView

urlpatterns = [
    path('bulk-discount/', BulkDiscountView.as_view(), name='bulk_discount'),
    path('order-discount/', OrderDiscountView.as_view(), name='order_discount'),
]
