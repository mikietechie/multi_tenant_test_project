from django.core.management.commands.migrate import Command as MigrationCommand

from tenants.models import Tenant, update_schema

class Command(MigrationCommand):
    def handle(self, *args, **kwargs):
        update_schema()
        super(Command, self).handle(*args, **kwargs)

            
