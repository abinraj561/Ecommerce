from django.urls import path
from rest_framework_simplejwt import views as jwtviews
from .views import *


urlpatterns =[
    path('refreshtoken/',jwtviews.TokenRefreshView.as_view(),name='refreshmenttoken'),
    path('acesstoken/',jwtviews.TokenObtainPairView.as_view(),name='acesstoken'),
    path('userregister/',UserRegister.as_view(),name='userregister'),
    path('login/',Login.as_view(),name='login'),
    path('userlist/',CustomerListView.as_view(),name='userlist'),
    path('userdetail/<int:pk>/',CustomerByIdView.as_view(),name='userlist'),
    path('password-reset/request/', PasswordResetView.as_view(), name='password_reset_request'),
    path('password-reset/<str:uidb64>/<str:token>/', ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
]