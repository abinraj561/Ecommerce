from .models import *
from django.contrib.auth.hashers import make_password
import django.contrib.auth.password_validation as validators
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import fields
from rest_framework import serializers
 
 
class UserRegistrationSerilaizer(serializers.ModelSerializer):
  
    class Meta:
        model = Customer
        fields="__all__"

    def validate_password(self, data):
        validators.validate_password(password=data,user=Customer)
        return data

    def save(self):
        
        reg = Customer(
                first_name = self.validated_data['first_name'],
                last_name = self.validated_data['last_name'],
                email = self.validated_data['email'],
                username = self.validated_data['username'],
                password = make_password(self.validated_data['password']),
                
            )
        reg.save()
        return reg
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 100)
    password = serializers.CharField(style = {"input_type":"password"})
   


class LoginResponseSerializer(serializers.ModelSerializer):
    access_token = serializers.SerializerMethodField()
    refresh_token = serializers.SerializerMethodField()
  
    def get_refresh_token(self,instance):
        return str(RefreshToken.for_user(instance))
   
    def get_access_token(self,instance):
        return str(RefreshToken.for_user(instance).access_token)
   
    class Meta:
        model = Customer
        fields=[
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "access_token",
            "refresh_token"
            
            ]


class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model =Customer
        fields=[
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            
            ]