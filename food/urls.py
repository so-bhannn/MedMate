from django.urls import path
from . import views

app_name='food'

urlpatterns = [
    path('random_food/', views.random_food_recipe, name='random_recipe')
]