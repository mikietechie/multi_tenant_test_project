from django.db import models, connection
from app.models import User
from .utils import install_fixtures
import os, sys


def set_active_db_schema(schema):
    with connection.cursor() as cursor:
            cursor.execute(f"SET search_path to {schema}")

def run_raw_sql(schema, sql):
    with connection.cursor() as cursor:
            cursor.execute(f"SET search_path to {schema}")
            cursor.execute(sql)

class Tenant(models.Model):
    name = models.CharField(max_length=64)
    schema = models.CharField(max_length=128)
    tenant_id = models.CharField(max_length=128, unique=True)
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.pk:
            super().save(*args,**kwargs)
            return
        with connection.cursor() as cursor:
            set_active_db_schema("public")
            super().save(*args,**kwargs)
            cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {self.schema}")
            cursor.execute(f"SET search_path to {self.schema}")
            python_launcher = 'python' if sys.platform.startswith("win32") else 'python3'
            os.system(f"{python_launcher} tenant_context_manage.py {self.schema} migrate")
            set_active_db_schema(self.schema)
            if self.schema != "public":
                run_raw_sql(
                    schema = self.schema,
                    sql = f"""
                    INSERT INTO tenants_tenant (id, name, schema, tenant_id) VALUES (1, '{self.name}', '{self.schema}', '{self.tenant_id}')
                    """
                )
            install_fixtures()
            if User.objects.count() == 0:
                user = User.objects.create(
                    username=f'{self.schema}-admin',
                    email=f"{self.schema}@mail.com",
                    is_superuser=True
                )
                user.set_password(f"{self.schema}password")
                user.save()
            set_active_db_schema("public")
        