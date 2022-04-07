from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager, PermissionsMixin)
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings


# Create your models here.
class Profile(models.Model):
    handle = models.CharField(max_length=50, default="Mike")
    rating = models.IntegerField(default=1400)
    virtual_rating = models.IntegerField(default=1400)

    def __str__(self):
        return self.handle


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if email is None:
            raise TypeError("Email not entered.")
        user_obj = self.model(username=username, email=email)
        user_obj.set_password(password)
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, username, email, password=None):
        if password is None:
            raise TypeError("Password not entered.")
        user_obj = self.create_user(username, email, password)
        user_obj.is_superuser = True
        user_obj.is_staff = True
        user_obj.is_active = True
        user_obj.save(using=self._db)
        return user_obj
    

class User(AbstractBaseUser, PermissionsMixin):
    email           =   models.EmailField(max_length = 255, unique = True, db_index = True)
    username        =   models.CharField(max_length = 255, unique = True, null = True, db_index = True)
    profile         =   models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE, related_name="user_profile")
    is_active       =   models.BooleanField(default = False)
    is_staff        =   models.BooleanField(default = False)
    password        =   models.CharField(max_length = 200)
    USERNAME_FIELD  =   'email'
    REQUIRED_FIELDS =   ['username']
    objects         =   UserManager()

    class Meta:
        db_table='user'

    def __str__(self):
        return self.email

    def token(self):
        refresh = RefreshToken.for_user(self)
        return str(refresh.access_token)
