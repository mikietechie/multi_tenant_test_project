from django.db import connection


def get_tenants_map():
    return  {
        "aone.co.zw": "aone",
        "bench.co.zw": "bench",
    }

def hostname_from_request(request):
    return request.get_host().split(":")[0].lower()

def tenant_from_request(request):
    hostname = hostname_from_request(request)
    tenants_map = get_tenants_map()
    return tenants_map.get(hostname)

def set_tenant_schema_for_request(request):
    schema = tenant_from_request(request)
    with connection.cursor() as cursor:
        cursor.execute(f"SET search_path to {schema}")
            