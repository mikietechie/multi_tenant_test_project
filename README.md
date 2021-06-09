to get started

run:

python manage.py makemigrations
python manage.py migrate
NB: after the above a public schema already exists
enter manage.py shell
run Tenant.objects.create(name="admin", tenant_id="admin", schema="public"); exit()
python tenant_context_manage.py public createsuperuser
done!