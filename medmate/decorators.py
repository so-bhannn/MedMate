from functools import wraps
from rest_framework.response import Response

def firebase_auth_required(view_func):
    @wraps(view_func)
    def wrapped_view(request,*args, **kwargs):
        if not request.firebase_user:
            return Response({'error': "Unauthorized User"}, status=401)
        return view_func(request,*args, **kwargs)
    return wrapped_view