from .models import Brand, Products
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .form import ProductForm, AddProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


@login_required(login_url="login_admin")
def home_view(request):
    brands = Brand.objects.all()
    return render(request, "home.html", {"brands": brands})


@login_required(login_url="login_admin")
def products_view(request, id):
    brands = Brand.objects.get(id=id)
    products = brands.products_set.all()
    return render(request, "products.html", {"products": products})

# delete product operation view


def delete_view(request, id):
    product = Products.objects.get(id=id)
    product.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


# edit product view operation
def edit__view(request, id):
    product = Products.objects.get(id=id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("home")
    form = ProductForm(instance=product)
    return render(request, "edit.html", {"form": form})


# add product
@login_required(login_url="login_admin")
def add_product_view(request):
    if request.method == "POST":
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
    form = AddProductForm()
    return render(request, "addproduct.html", {"form": form})


# about
def about_view(request):
    return render(request, "about.html", {})

# auth system


def login_view(request):
    msg = ""
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            msg = "User is not authenticated"
    return render(request, "login.html", {"msg": msg})


def logout_view(request):
    logout(request)
    return redirect("login_admin")
