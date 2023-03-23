from django.shortcuts import render
from django.urls import path 
from . import views 


urlpatterns = [
    
    path('', views.HelloAuthView.as_view(),name='hello_auth'),
    path('signup/',views.UserCreateView.as_view(),name='sign_up'),
    path("login/",views.UserLoginView.as_view(),name="login")
    
    
]
