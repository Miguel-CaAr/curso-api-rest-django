from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import (
    BasicAuthentication, SessionAuthentication, TokenAuthentication) # Middlewares que interceptan la peticion
from rest_framework.permissions import IsAuthenticated # Validan si se esta autenticado
from rest_framework_simplejwt.authentication import JWTAuthentication # type: ignore
from rest_framework_simplejwt.tokens import RefreshToken # type: ignore
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)
            context = {
                'status': True,
                'content': {
                        'username':user.username,
                        'token':str(refresh.access_token)
                    }
            }
        else:
            context = {
                'status': False,
                'content': 'Credenciales no validas'
            }
            
        return Response(context)