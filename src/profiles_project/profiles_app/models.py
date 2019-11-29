from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
class UserProfileManager(BaseUserManager):
    """Works with custom user model"""
    def create_user(self,email,name,password=None):
        """Creates a new user profile Object"""

        if not email :
            raise ValueError('User Must have a Valid Email Address')
        email=self.normalize_email(email)
        user =self.model(email = email , name = name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self , email , name , password):
        """Creates and saves a new superuser"""
        user = self.create_user(email , name , password)
        user.is_superuser = True
        user.is_staff     = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser , PermissionsMixin):
    """Represents User Profile"""
    email = models.EmailField(max_length=255 , unique=True)
    name  = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff  = models.BooleanField(default=False)

    object = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Used to get a users full name"""
        return self.name

    def get_short_name(self):
        """Used to get a users short name"""
        return self.name

    def __str__(self):
        """Converts object to string"""
        return self.email

class ProfileFeedItem(models.Model):
    """Profile Status Update"""
    user_profile = models.ForeignKey('UserProfile',on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Converts object to string"""
        return self.status_text
