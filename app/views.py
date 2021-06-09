from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Branch, User
from tenants.models import Tenant
from django.db import connection


def login_view(request):
    if request.method == "POST":
        tenant_id = request.POST.get("tenant_id")
        username = request.POST.get("username")
        password = request.POST.get("password")
        request.session["tenant_id"] = tenant_id
        with connection.cursor() as cursor:
            cursor.execute(f"SET search_path to {tenant_id}")
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
    if request.method == "POST":
        name = request.POST.get("name")
        city = request.POST.get("city")
        Branch.objects.create(name=name, city=city)
        return HttpResponseRedirect(reverse("index"))
    context = dict(
        branches = Branch.objects.all()
    )
    return render(request, 'app/index.html', context=context)