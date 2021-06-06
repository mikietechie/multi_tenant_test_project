from django.contrib import admin
from .models import Tenant
from app.utils import set_tenant_schema_for_request,tenant_from_request

# Register your models here.

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    
    def get_queryset(self, request, *args, **kwargs):
        set_tenant_schema_for_request(request)
        queryset = super().get_queryset(request, *args, **kwargs)
        tenant = tenant_from_request(request)
        if tenant.schema != "public":
            queryset = queryset.filter(schema=schema)
        return queryset
    
    def save_model(self, request, obj, form, change):
        set_tenant_schema_for_request(request)
        tenant = tenant_from_request(request)
        if tenant.schema == "public":
            super().save_model(request, obj, form, change)
            return
        
        raise Exception("Only the software providers can create tenants!!!")