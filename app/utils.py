from django.db import connection


from tenants.models import Tenant

def hostname_from_request(request):
    return request.get_host().split(":")[0].lower()

def tenant_from_request(request):
    hostname = hostname_from_request(request)
    return Tenant.objects.get(subdomain_prefix=hostname)

def set_tenant_schema_for_request(request):
    schema = tenant_from_request(request)
    with connection.cursor() as cursor:
        cursor.execute(f"SET search_path to {schema}")
            