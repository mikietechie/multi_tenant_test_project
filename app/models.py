from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Tenant(models.Model):
    name = models.CharField(max_length=64)
    subdomain_prefix = models.CharField(max_length=100, unique=True)


class TenantAwareModel(models.Model):
    tenant = models.ForeignKey('Tenant', related_name='', on_delete=models.CASCADE)

    class Meta:
        abstract = True
'''  
class Branch(TenantAwareModel):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
'''

class Branch(models.Model):
    
    tenant = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
