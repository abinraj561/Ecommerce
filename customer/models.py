from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission

# Create your models here.

class Customer(AbstractUser):
    first_name = models.CharField(max_length=50,null=True)
    last_name = models.CharField(max_length=50,null=True)
    username=models.CharField(max_length=50,null=True,unique=True)
    phone = models.CharField(max_length=15,null=True,unique=True)
    email = models.EmailField(null=True,unique=True)
    password = models.CharField(max_length=500,null=True)
    groups = models.ManyToManyField(Group, related_name='user_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='user_permissions', blank=True)


