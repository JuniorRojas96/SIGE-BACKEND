from django.contrib import admin
from django.urls import path, re_path
from . import views
from accounts import views
from rest_framework.documentation import include_docs_urls 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.getRoutes),
    path("docs/", include_docs_urls(title="Auth API")), 
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('qr-code/', views.QRCodeView.as_view(), name='qr-code-generate'),
    
    path('users/', views.UsersListCreateView.as_view() ),
    
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token),


]

