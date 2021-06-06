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
        super().save(*args,**kwargs)
        # TODO: implement correct logic to trigger the creation of a schema on the initial save of a tenant
        '''
        currently do the following:
            - manage.py makemigrations
            - manage.py migrate
            - manage.py migrate_schemas
            - tenant_context_manage.py public createsuperuser
            - in manage.py shell create a tenant with (name: admin, domain: localhost, schem: public)
            - visit admin create more tenants
            - manage.py migrate_schemas
            - repeat for all tenants
            - tenant_context_manage.py tenant_schema createsuperuser
            done
        '''
        '''
        if self.pk:
            super().save(*args,**kwargs)
            return
        super().save(*args,**kwargs)
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {self.schema}")
            cursor.execute(f"SET search_path to {self.schema}")
            python_launcher = 'python' if sys.platform.startswith("win32") else 'python3'
            os.system(f"{python_launcher} tenant_context_manage.py aone migrate")
            set_active_db_schema(self.schema)
            if User.objects.count() == 0:
                User.objects.create(
                    username=f'{self.schema} admin',
                    email=f"{self.schema}@mail.com",
                    password=f"{self.schema}password",
                    is_superuser=True
                )
            set_active_db_schema("public")
        '''
            
            
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
        