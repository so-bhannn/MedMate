from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

@api_view(['GET'])
def foodfact(request):
    try:
        if not request.firebase_user:
            return Response({'error': "Unauthorized User"}, status=401)
        
        header = {
            'x-api-key': '9ec257f0852b4fb8994b1128e7b27c81',
        }

        response = requests.get('https://api.spoonacular.com/food/trivia/random', headers=header)
        data = response.json()
        return Response(data)
    
    except Exception as e:
        return Response({'error':str(e)}, status=500)