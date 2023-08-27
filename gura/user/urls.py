from django.urls import path, include
from . import views
# for login AND SIGN UP
from .views import CustomLoginView, SignUpView, PasswordResetView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
]
