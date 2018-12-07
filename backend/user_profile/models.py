from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40, null=True, blank=True)
    last_name = models.CharField(max_length=40, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
