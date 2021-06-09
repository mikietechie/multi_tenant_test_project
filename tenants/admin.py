from django.contrib import admin
from .models import Tenant

# Register your models here.

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    
    def save_model(self, request, obj, form, change):
        if request.session['tenant_id'] == "public":
            super().save_model(request, obj, form, change)
            return
        
        raise Exception("Only the software providers can create tenants!!!")