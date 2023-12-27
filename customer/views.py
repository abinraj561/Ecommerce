import datetime
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework import filters,status
from customer.models import *
from ecommerce import settings
from rest_framework import generics,permissions,status
from .signals import send_registration_email
import smtplib
from django.core.mail import send_mail
from .serializers import *
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.template.loader import render_to_string


""" User registration"""

class UserRegister(generics.CreateAPIView):
     
    def get_serializer_class(self):
        return UserRegistrationSerilaizer
 
    def create(self,request,*args,**kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response({'message': 'Error in Registration', 'errors': e.detail}, status=status.HTTP_304_NOT_MODIFIED)

    def perform_create(self,serializer):
        serializer.save()

""" User Login """ 

class Login(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
 
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
           
            try:
                user_obj = Customer.objects.get(
                    Q(username__iexact=data["username"]) | Q(email__iexact=data["username"])
                )
                if user_obj and check_password(data["password"], user_obj.password):
                    user_obj.last_login = datetime.datetime.now()
                    user_obj.save()
                    refresh_token = RefreshToken.for_user(user_obj)
                    response_serializer = LoginResponseSerializer(instance=user_obj)
                    return Response(response_serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "Invalid Password", "status": "1"})
            except Customer.DoesNotExist:
                return Response({"message": "Invalid User", "status": "1"})
            except Exception as e:
                print("Login Error:", str(e))
                return Response({"message": "An error occurred during login", "status": "1"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

""" Users list """ 

class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    permission_classes=[permissions.IsAdminUser]
    serializer_class = UserListSerializers
    
    def get_queryset(self):
        try:
            queryset = Customer.objects.all()
            return queryset
        except Exception as e:
            return Response({'message': 'Error in Retrieving', 'errors': e.detail}, status=status.HTTP_404_NOT_FOUND)

""" User view by id """ 

class CustomerByIdView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Customer.objects.all()
    serializer_class = UserListSerializers
    permission_classes = [permissions.IsAdminUser]
 
    def delete(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            return Response({'message': 'Deleted successfully'})
        except Exception as e:
            return Response({'message': 'Error in deleting', 'errors': e.detail}, status=status.HTTP_304_NOT_MODIFIED)

""" Password  Reset """ 

class PasswordResetView(APIView):
    def post(self, request):
        email = request.data.get('email','')
        try:
            user = Customer.objects.get(email=email)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = f'http://your-domain/reset-password/{uid}/{token}/'
            message =f'Click the link to reset the password :{reset_link}'
            html_message=render_to_string('password_reset.html',{'reset_link':reset_link})
            html_message=render_to_string('password_reset.html',{'reset_link':reset_link})
            subject='Password Reset'
            send_mail(
                subject,
                message,
                "admin@gmail.com",
                [email],
                html_message=html_message,
                fail_silently=False,
            )

            return Response({'message': 'Password reset email sent'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

""" Password Confirmation """ 

class ResetPasswordConfirmView(APIView):
    permission_classes=[permissions.AllowAny]
    def get(self,request,uidb64,token):
        try:
            uid=str(urlsafe_base64_decode(uidb64),'utf-8')
            user=Customer.objects.get(pk=uid)

            if default_token_generator.check_token(user, token):
                return Response({'message':'new Password','uidb64':uidb64,'token':token})
            else:
                return Response({'message':'Invalid link'})
            
        except (TypeError,ValueError,OverflowError,Customer.DoesNotExist):
            return Response({'message':'invalid link'})
        

    def post(self,request,uidb64,token):
        try:
            uid=str(urlsafe_base64_decode(uidb64),'utf-8')
            user=Customer.objects.get(pk=uid)

            if default_token_generator.check_token(user, token):
                new_password=request.data.get('new_password')

                if new_password:
                    user.password =make_password(new_password)
                    user.save()
                    return Response({'message':'Successfully updated Password '},status=status.HTTP_200_OK)
                else:
                    return Response({'message':'Provide new Password'},status=status.HTTP_400_BAD_REQUEST)
            
            else:
                return Response({'message':'Invalid link'})
            
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
