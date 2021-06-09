from django.db import connection


class TenantMiddleware:
    def __init__(self, get_response):
        with connection.cursor() as cursor:
            cursor.execute(f"SET search_path to public")
            self.get_response = get_response
    
    def __call__(self, request):
        with connection.cursor() as cursor:
            active_schema = "public" if not request.session.get("tenant_id") else request.session["tenant_id"]
            cursor.execute(f"SET search_path to public")
            response = self.get_response(request)
            return response
