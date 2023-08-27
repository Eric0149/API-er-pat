from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CartItem, Order
from product.models import Product
from .serializers import ProductSerializer, CartItemSerializer, OrderSerializer
# for orders
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
import secrets

# imports of Documentations

# rate limiting to orders placed per min by same user
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        
        return render(request, "product_list.html", {"products":serializer.data})
class CartView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = self.request.user
        cart_items = CartItem.objects.filter(user=user)
        serializer = CartItemSerializer(cart_items, many=True)
        return render(request, 'cart_list.html', {'cart_items' : serializer.data})

class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
       user = self.request.user
       order_items = Order.objects.filter(user=user)
       serializer = OrderSerializer(order_items, many=True)
       return render(request, 'order_list.html', {'order_items' : serializer.data})

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class PlaceOrderView(APIView):
    throttle_classes = [UserRateThrottle]

    def post(self, request):
        user = self.request.user  # Get the authenticated user
        order_data = {"user": user.id, "other_fields": "values"}  # Create order data
        
        serializer = OrderSerializer(data=order_data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Order placed successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            order_token = secrets.token_urlsafe(16)
            order = serializer.save(user=request.user, token=order_token)
            # Any additional logic related to order creation
            return Response({'message': 'Order created successfully'}, status=201)
        return Response(serializer.errors, status=400)

