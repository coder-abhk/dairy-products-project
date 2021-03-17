from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("products/<int:id>", views.products_view, name="products"),
    path("delete/<int:id>", views.delete_view, name="delete"),
    path("edit/<int:id>", views.edit__view, name="editProduct"),
    path("login", views.login_view, name="login_admin"),
    path("logout", views.logout_view, name="logout_admin"),
    path("addproduct", views.add_product_view, name="addproduct"),
    path("about", views.about_view, name="about")
]
