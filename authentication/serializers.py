from .models import User
from rest_framework import serializers


class UserCreationSerializer(serializers.ModelSerializer):
    username=serializers.CharField(max_length=25)
    email=serializers.EmailField(max_length=80)
    phone_number=PhoneNumberField(allow_null=False,allow_blank=False) 