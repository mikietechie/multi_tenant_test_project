from django.shortcuts import render
from django.http import HttpResponse

from .models import Branch, User
from .utils import set_tenant_schema_for_request,tenant_from_request

def login_view(request):
    if request.method == "POST":
        request.session["tenant_id"] = request.POST.get("tenant_id")
        set_tenant_schema_for_request(request)
        user = User.objects.get(
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )
    return render(request, 'app/login.html')

def index_view(request):
    set_tenant_schema_for_request(request)
    tenant = tenant_from_request(request)
    context = dict(
        branches = Branch.objects.filter(tenant=tenant)
    )
    return render(request, 'app/index.html', context=context)