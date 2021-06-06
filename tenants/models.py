from django.db import models, connection
import os, sys


def update_schema():
    with connection.cursor() as cursor:
        for tenant in Tenant.objects.all():
            cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {tenant.schema}")
            cursor.execute(f"SET search_path to {tenant.schema}")


class Tenant(models.Model):
    name = models.CharField(max_length=64)
    schema = models.CharField(max_length=128)
    domain = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.pk:
            super().save(*args,**kwargs)
            return
        super().save(*args,**kwargs)
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {self.schema}")