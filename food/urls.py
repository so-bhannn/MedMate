from django.urls import path
from . import views

urlpatterns = [
    path('random_food/', views.random_food_recipe, name='random_recipe')
]