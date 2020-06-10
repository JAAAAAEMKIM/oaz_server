from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

class UserInfo(models.Model):
    owner = models.OneToOneField(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    Introduction = models.TextField()
    mobile = models.CharField(
        default='', max_length=255, verbose_name="전화번호")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # TODO: profile_pic
     