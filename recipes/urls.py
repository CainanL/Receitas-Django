from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>', views.recipe)  # <id> -> id como parametro; <int:id> id do tipo inteiro como parametro
]
