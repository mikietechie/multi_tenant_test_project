echo making tenant migrations
manage.py makemigrations tenants
manage.py migrate
echo migrated tenants
manage.py migrate_schemas
manage.py makemigrations
manage.py migrate
echo did all migrations