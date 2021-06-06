from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass


class TenantAwareModel(models.Model):
    tenant = models.ForeignKey('tenants.Tenant', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        abstract = True

class Branch(TenantAwareModel):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)

    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'

    def __str__(self):
        return self.name

