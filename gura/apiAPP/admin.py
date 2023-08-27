from django.contrib import admin
from .models import CartItem
from .models import Order, OrderItem
# Register your models here.

@admin.register(CartItem)
class CartItemtAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_date', 'total_price')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'subtotal')
