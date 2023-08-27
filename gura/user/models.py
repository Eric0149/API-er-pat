from django.db import models
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import PasswordResetView

# Create your models here.

# creating profile for custom

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'



