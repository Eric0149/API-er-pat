from django.shortcuts import render
from .models import Product

def home(request):
    posts = Product.objects.all()
    return render(request, 'product/home.html', {'posts': posts})
