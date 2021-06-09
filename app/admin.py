from django.contrib import admin
from .models import User, Branch


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    pass

        