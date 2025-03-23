from rest_framework.decorators import api_view
from rest_framework.response import Response
from medmate.decorators import firebase_auth_required
import requests
from decouple import config
import random

# Create your views here.

@firebase_auth_required
@api_view(['GET'])
def random_food_recipe(request):
    
    try:
        header={
            'x-api-key': config('SPOONACULAR_API_KEY'),
        }

        param={
            'query': 'healthy',
            'instructionRequired': 'true',
            'addRecipeNutrition': 'true',
            'offset' : random.randit(1,100),
            'number': 5
        }

        response=requests.get('https://api.spoonacular.com/recipes/complexSearch',headers=header,params=param)
        data = response.json()
        return Response(data)

    except Exception as e:
        return Response({'error':str(e)},status=500)