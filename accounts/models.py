from .managers import UserManager
from django.db import models
from django.contrib.auth.models import AbstractUser , PermissionsMixin


class CustomUser(AbstractUser , PermissionsMixin):
    username = None
    phone_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=100)
    job = models.CharField(max_length=100, blank=True, null=True)
    is_legal = models.BooleanField(default=False)

    # objects = UserManager()
    UserManagers = UserManager()
    # objects = UserManager



    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ('email' ,'full_name')
    
class Kid(models.Model):
    pass
    # list_relative = (("pedar", "پدر"),("daii", "دایی"),("amo", "عمو"),)
    # relative = models.CharField(choise=list_relative, max_length=20)
    # relative_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # qad = models.IntegerField()
    # vazn = models.IntegerField()
    #  age = models.IntegerField()
    # sex =models.BooleanField()
    # numx = models.IntegerField()
