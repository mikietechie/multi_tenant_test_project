from django.contrib import admin
from .models import Tenant

# Register your models here.

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    pass