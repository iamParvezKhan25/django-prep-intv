from django.db import models

# Create your models here.

from django.db import models
from colorfield.fields import ColorField

from prep_app.models import ApplicationUser


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = "tbl_category"

    def __str__(self):
        return self.name


class Colour(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    colour = ColorField(default='#FF0000')

    class Meta:
        db_table = 'tbl_colour'

    def __str__(self):
        return self.colour


class Size(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_size'

    def __str__(self):
        return self.name


class DeliveryTime(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'tbl_delivery_time'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    seller = models.ForeignKey(ApplicationUser, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_product'

    def __str__(self):
        return self.name


class SubProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    color = models.ForeignKey(Colour, on_delete=models.CASCADE, null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True, blank=True)

    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_time = models.ForeignKey(DeliveryTime, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_sub_product'

    def __str__(self):
        return f"{self.product.name} - {self.color} - {self.size}"


class Stock(models.Model):
    sub_product = models.ForeignKey(SubProduct, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        db_table = 'tbl_stock'

    def __str__(self):
        return f"{self.sub_product.product.name} - {self.quantity}"


class Images(models.Model):
    sub_product = models.ForeignKey(SubProduct, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')

    class Meta:
        db_table = 'tbl_images'

    def __str__(self):
        return f"{self.sub_product.product.name} - {self.image}"
