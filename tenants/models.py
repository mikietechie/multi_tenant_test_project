from django.db import models, connection
from app.models import User
import os, sys


def set_active_db_schema(schema):
    with connection.cursor() as cursor:
            cursor.execute(f"SET search_path to {schema}")


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
        '''
        To add logic to create a super user instance of a new tenant
        set_active_db_schema(self.schema)
        User.objects.create(
            username=f'{self.schema} admin',
            email=f"{self.schema}@mail.com",
            password=f"{self.schema}password",
            is_superuser=True
            )
        set_active_db_schema("public")
        '''
        