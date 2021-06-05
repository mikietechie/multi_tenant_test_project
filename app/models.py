from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Company(models.Model):
    name = models.CharField(max_length=64)
    tenant_id = models.CharField(max_length=128)