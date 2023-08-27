from typing import Any

from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# class Photo(models.Model):
#     title = models.CharField(max_length=100)

# def __str__(self):
#     return self.title


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

