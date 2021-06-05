from django.core.management.commands.migrate import Command as MigrationCommand

from django.db import connection
from tenants.models import Tenant


class Command(MigrationCommand):
    def handle(self, *args, **kwargs):
        with connection.cursor() as cursor:
            for tenant in Tenant.objects.all():
                cursor.execute(f"CREATE SCHEMA IF NOT EXISTS {tenant.schema}")
                cursor.execute(f"SET search_path to {tenant.schema}")
                super(Command, self).handle(*args, **kwargs)

            
