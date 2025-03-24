from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services.gemini_api import verified_response
from medmate.decorators import firebase_auth_required
# Create your views here.

@firebase_auth_required
@api_view(['POST'])
def chat(request):
    try:
        user=request.firebase_user.get("uid")
        email=request.firebase_user.get("email")
        query=request.data.get("query")
        if not query:
            return Response({"error":"Query is required"}, status=400)
        
        response=str(verified_response(query=query))
        return Response({
            "user":user,
            "email":email,
            "response":response,
        })
    
    except Exception as e:
        print(f'Chat Error: {str(e)}')
        return Response({"error":"An expected error occured."}, status=500)