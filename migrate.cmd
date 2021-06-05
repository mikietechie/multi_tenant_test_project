echo making tenant migrations
manage.py makemigrations tenants
manage.py migrate
echo migrated tenants
manage.py migrate_schemas
manage.py makemigrations
manage.py migrate
echo did all migrations

echo Do you want to create an initial tenant [y/n]
set /p wants_to_create_a_tenant = 
if "%wants_to_create_a_tenant%" == "n" goto has_tenants_already
echo Copy and Paste the following lines one at a time in your shell
echo from tenants.models import Tenant
echo Tenant.objects.create(name='admin', domain='admin.co.zw', schema='public')
echo exit()
manage.py shell
echo Tenant must be successfully created
goto has_tenants_already

:has_tenants_already
echo Do you want to create an initial super user for the admin-public schema [y/n]
set /p wants_to_create_a_superuser = 
if "%wants_to_create_a_superuser%" == "n" goto finish
manage.py createsuperuser
goto finish

:finish
echo Done!!!
