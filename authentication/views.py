from django.shortcuts import render
from rest_framework import generics,status 
from rest_framework.response import Response
from . import serializers
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your views here.

class HelloAuthView(generics.GenericAPIView):
    def get(self,request):
        return Response(data={"message":"Hello Auth"},status=status.HTTP_200_OK)
        
        
class UserCreateView(generics.GenericAPIView):
    
    serializer_class=serializers.UserCreationSerializer
    

    def post(self,request):
        data=request.data
        
        serializer=self.serializer_class(data=data)
        email = request.data.get('email')
        print(email)
        user = User.objects.filter(email=email)
        
        if user.exists():
            return Response({
                'status': False,
                'message': 'User with this email exists'
            }, status=status.HTTP_403_FORBIDDEN)
        
        
        
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
class UserLoginView(generics.GenericAPIView):
    
    serializer_class=serializers.UserLoginSerializer   
    
    
    
    
    def post(self,request):
        data=request.data 
        
        
        serializer=self.serializer_class(data=data)
        if not serializer.is_valid():
            return Response({
                'status':False,
                'message': 'invalid data provided',
                "errors": serializer.errors
                

            })
        
        
            
        
        email = request.data.get('email')
        print(email)
        user = User.objects.filter(email=email)
        
        if  not user.exists():
            return Response({
                'status': False,
                'message': 'User with this email  does not exists'
            }, status=status.HTTP_403_FORBIDDEN)
    
    
       