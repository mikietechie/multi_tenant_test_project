from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Branch, User
from .utils import set_tenant_schema_for_request,tenant_from_request


def login_view(request):
    if request.method == "POST":
        tenant_id = request.POST.get("tenant_id")
        username = request.POST.get("username")
        password = request.POST.get("password")
        request.session["tenant_id"] = tenant_id
        set_tenant_schema_for_request(request)
        user = authenticate(
            request=request,
            username=username,
            password=password
        )
        for u in User.objects.all():
            print(u.username, u.password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "app/login.html", {"message": "Invalid credentials!"})
    return render(request, 'app/login.html')

#@login_required(login_url='login')
def index_view(request):
    set_tenant_schema_for_request(request)
    tenant = tenant_from_request(request)
    if request.method == "POST":
        print("hit")
        name = request.POST.get("name")
        city = request.POST.get("city")
        Branch.objects.create(tenant=tenant, name=name, city=city)
        return HttpResponseRedirect(reverse("index"))
        
    context = dict(
        branches = Branch.objects.filter(tenant=tenant)
    )
    return render(request, 'app/index.html', context=context)