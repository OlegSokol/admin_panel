from django.db import models


class Product(models.Model):
    product_number = models.BigIntegerField(null=False, serialize=True)
    description = models.CharField(max_length=200)
    image_id = models.CharField(max_length=200)
    price = models.BigIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Order(models.Model):
    order_number = models.BigIntegerField(null=False, serialize=True)
    customer_name = models.CharField(max_length=200)
    customer_surname = models.CharField(max_length=200)
    customer_email = models.CharField(max_length=200)
    order_products = models.ManyToManyField(Product)
    total_price = models.BigIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
