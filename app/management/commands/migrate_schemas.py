from django.core.management.commands.migrate import Command as MigrationCommand

from django.db import connection
from tenants.models import Tenant
from app.models import User


class Command(MigrationCommand):
    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            if Tenant.objects.count() == 0:
                Tenant.objects.create(name="admin", domain="admin", schema="public")
            if User.objects.filter(is_superuser=True).count() == 0:
                User.objects.create(username="admin", email="admin@admin.com", password="admin1234", is_superuser=True)
            for tenant in Tenant.objects.all():
                cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {tenant.schema}")
                cursor.execute(f"SET search_path to {tenant.schema}")
                super(Command, self).handle(*args, **kwargs)

            
