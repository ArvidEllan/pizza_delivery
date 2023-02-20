from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class CustomUserManager(BaseUserManager):
    
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError(_("email should be provided"))
        email=self.normalize_email(email)
        
        new_user=self.model(email,**extra_fields)
        
        new_user.set_password(password)
        
        new_user.save()
        
        return new_user
    
    def create_superuser(self,email,password,**extra_fields):
        pass 
