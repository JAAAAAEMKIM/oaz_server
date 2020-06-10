from django.db import models
from users.models import User

# Create your models here.

# Managed By Django Admin Page
class Notice(models.Model):
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)