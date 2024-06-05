from rest_framework import generics
from .serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import (
    BasicAuthentication, SessionAuthentication, TokenAuthentication) # Middlewares que interceptan la peticion
from rest_framework.permissions import IsAuthenticated # Validan si se esta autenticado

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]