from django.shortcuts import render
from django.http import HttpResponse

from .models import Branch
from .utils import set_tenant_schema_for_request,tenant_from_request

def index_view(request):
    set_tenant_schema_for_request(request)
    tenant = tenant_from_request(request)
    context = dict(
        branches = Branch.objects.filter(tenant=tenant)
    )
    return render(request, 'app/index.html', context=context)