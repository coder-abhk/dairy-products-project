from django.db import models


class Brand(models.Model):
    brand_name = models.CharField(max_length=55, null=False)

    def __str__(self):
        return self.brand_name

    class Meta:
        verbose_name_plural = "Brands"


class Products(models.Model):
    product_name = models.CharField(max_length=55, null=False)
    product_price = models.IntegerField(default=0, null=False)
    product_weight = models.IntegerField(default=0, null=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = "Products"
