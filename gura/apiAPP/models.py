from django.db import models
from product.models import Product
from user.models import CustomLoginView
from django.contrib.auth.models import User

#for tokens and other stuffs
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
import secrets

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=3, null=True)

    def __str__(self):
        return f"Cart item: {self.product}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    products = models.ManyToManyField(Product, through='OrderItem')
    token = models.CharField(max_length=32, unique=True)  # Add token field

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"
    
@login_required
class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.order.id} - {self.product.name}"


@login_required
def create_order(request):
    order_token = secrets.token_urlsafe(16)
    order = Order.objects.create(user=request.user, total_price=any, token=order_token)
    # Any additional logic related to order creation
    return redirect('products')
