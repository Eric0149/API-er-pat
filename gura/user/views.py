from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import PasswordResetView


# Create your views here.
def login(request):
    credit = login.objects.all()
    return render(request, 'registration/login.html', {'credit': credit})


# for login
class CustomLoginView(LoginView):
    template_name = 'login.html'


# for signing up
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


# for password restting
class PasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'

# making APIs
# for retrieving users
