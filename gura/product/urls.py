from django.urls import path, include
from . import views
urlpatterns = [
    path('product/', include("apiAPP.urls")),
    path('', views.home, name='home')

]
