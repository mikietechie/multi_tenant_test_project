from django.db import models

# Create your models here.

class Tenant(models.Model):
    name = models.CharField(max_length=64)
    schema = models.CharField(max_length=128)
    domain = models.CharField(max_length=100, unique=True)