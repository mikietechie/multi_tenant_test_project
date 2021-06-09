from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Branch, User
from tenants.models import Tenant
from .utils import set_tenant_schema_for_request,tenant_from_request
from django.db import connection
            
def login_view(request):
    if request.method == "POST":
        tenant_id = request.POST.get("tenant_id")
        username = request.POST.get("username")
        password = request.POST.get("password")
        request.session["tenant_id"] = tenant_id
        set_tenant_schema_for_request(request)
        tenant = Tenant.objects.get(tenant_id=tenant_id)
        with connection.cursor() as cursor:
            cursor.execute(f"SET search_path to {tenant.schema}")
            user = authenticate(
                request=request,
                username=username,
                password=password
            )
            if user is not None:
                cursor.execute(f"SET search_path to public")
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                return render(request, "app/login.html", {"message": "Invalid credentials!"})
    return render(request, 'app/login.html')

#@login_required(login_url='login')
def index_view(request):
    set_tenant_schema_for_request(request)
    tenant = tenant_from_request(request)
    with connection.cursor() as cursor:
        print(tenant.schema)
        cursor.execute(f"SET search_path to {tenant.schema}")
        if request.method == "POST":
            name = request.POST.get("name")
            city = request.POST.get("city")
            Branch.objects.create(tenant=Tenant.objects.get(pk=1), name=name, city=city)
            return HttpResponseRedirect(reverse("index"))
            
        context = dict(
            branches = Branch.objects.all()
        )
        return render(request, 'app/index.html', context=context)