from django.shortcuts import render
from rest_framework import generics,status 
from rest_framework.response import Response
from . import serializers
from django.contrib.auth import get_user_model, authenticate
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
        
        if not serializer.is_valid():
            
                return Response({
                    'message':'invalid information',
                    'status':status.HTTP_400_BAD_REQUEST,
                    'errors': serializer.errors})
                
                
                    
        
    
        
        email = request.data.get('email')
        print(email)
        user = User.objects.filter(email=email)
        
        if user.exists():
            return Response({
                'status': False,
                'message': 'User with this email exists'
            }, status=status.HTTP_403_FORBIDDEN)
        
        else:
            return Response({
                
                'status':True,
                'message':'User registered succesfully',
                'status':status.HTTP_201_CREATED
                
            })
        
    
        
class UserLoginView(generics.GenericAPIView):
    
    serializer_class=serializers.UserLoginSerializer    
    
    def post(self,request):
        data=request.data 
        user=request.user
        
        
        
        serializer=self.serializer_class(data=data)
        if not serializer.is_valid():
            return Response({
                'status':False,
                'message': 'invalid data provided',
                "errors": serializer.errors
            })
        
        email = request.data.get('email')
        password = request.data.get('password')
        
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        valid_email = re.fullmatch(email_regex, email)
        
        user = User.objects.filter(email=email)
        if not user.exists():
            return Response({
                'status': False,
                'message': 'User with this email does not exist, kindly sign up'
            }, status=status.HTTP_404_NOT_FOUND)
    
        
        
    
        user =authenticate(username=email,password=password)
        
        if user is None:
            return Response ({
                
                'status' : False,
                'message' : 'provide correct password and username'  
                
            })
    
       