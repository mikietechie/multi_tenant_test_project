from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass


class TenantAwareModel(models.Model):
    tenant = models.ForeignKey('tenants.Tenant', on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Branch(TenantAwareModel):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
