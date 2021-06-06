from django.db import connection


from tenants.models import Tenant, set_active_db_schema

def hostname_from_request(request):
    return request.get_host().split(":")[0].lower()

def tenant_from_request(request):
    hostname = hostname_from_request(request)
    set_active_db_schema("public")
    return Tenant.objects.get(domain=hostname)

def set_tenant_schema_for_request(request):
    tenant = tenant_from_request(request)
    with connection.cursor() as cursor:
        cursor.execute(f"SET search_path to {tenant.schema}")
            