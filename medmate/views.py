from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from decouple import config
from .decorators import firebase_auth_required

@firebase_auth_required
@api_view(['GET'])
def foodfact(request):
    try:        
        header = {
            'x-api-key': config('SPOONACULAR_API_KEY'),
        }

        response = requests.get('https://api.spoonacular.com/food/trivia/random', headers=header)
        data = response.json()
        return Response(data)
    
    except Exception as e:
        return Response({'error':str(e)}, status=500)