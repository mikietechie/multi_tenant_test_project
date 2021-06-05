from django.db import models

# Create your models here.

class Tenant(models.Model):
    name = models.CharField(max_length=64)
    subdomain_prefix = models.CharField(max_length=100, unique=True)