from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

class UserProfileManager(BaseUserManager):
    #Helps django to work with our custom user model
    def create_user(self,email,name,password=None):
        #Creates new user profile
        if not email:
            raise ValueError('USERS MUST HAVE AN EMAIL ADDRESS')

        email = self.normalize_email(email)
        user  = self.model(email = email , name = name)
        user.set_password(password)
        user.save(using = self._db)

        return user

    def create_superuser(self,email,name,password):
        #Creates new SuperUser Profile
        user = self.create_user(email,name,password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using = self._db)

        return user


class UserProfile(AbstractBaseUser , PermissionsMixin):
    #Represents User Profile inside our system
    email = models.EmailField(max_length = 255 , unique = TRUE)
    name = models.CharField(max_length = 255)
    is_active = models.BooleanField(default = TRUE)
    is_staff = models.BooleanField(default = FALSE)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        #Will get the user full name
        return self.name

    def get_short_name(self):
        #Will get the user short name
        return self.name

    def __str__(self):
        #Django uses this to convert object to string
        return self.email
