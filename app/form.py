from django.forms import ModelForm
from .models import Products


class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ["product_name", "product_price", "product_weight"]


class AddProductForm(ModelForm):
    class Meta:
        model = Products
        fields = ["product_name", "product_price", "product_weight", "brand"]
