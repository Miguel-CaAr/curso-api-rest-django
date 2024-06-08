from rest_framework import serializers
# Importamos el modelo de usuario proporcionado por defecto por django
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        # Aqui se especifica que el campo de password solo sera de escritura no de visualizacion
        extra_kwargs = {'password': {'write_only': True}}

    # Poliformismo de sobreescritura del metodo 'create' para encriptar el password
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer #type:ignore

class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token = super().get_token(user)
        
        token['username'] = user.username
        token['fullname'] = user.first_name + ' ' + user.last_name
        
        return token        