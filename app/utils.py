from django.db import connection


from tenants.models import Tenant, set_active_db_schema

def tenant_id_from_request(request):
    return request.session.get("tenant_id")

def tenant_from_request(request):
    tenant_id = tenant_id_from_request(request)
    set_active_db_schema("public")
    return Tenant.objects.get(tenant_id=tenant_id)

def set_tenant_schema_for_request(request):
    if "login" in request.META.get("PATH_INFO"):
        with connection.cursor() as cursor:
            cursor.execute("SET search_path to public")
    else:
        tenant = tenant_from_request(request)
        with connection.cursor() as cursor:
            cursor.execute(f"SET search_path to {tenant.schema}")
            