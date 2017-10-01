from django.db import models


class Category(models.Model):
    id = models.BigIntegerField(null=False, serialize=True, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)

    def __str__(self):
        return str(self.id) + '  ' + str(self.name)


class Product(models.Model):
    id = models.BigIntegerField(null=False, serialize=True, primary_key=True)
    description = models.CharField(max_length=200)
    image_id = models.CharField(max_length=200)
    price = models.BigIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id) + '  ' + str(self.description)


class Order(models.Model):
    id = models.BigIntegerField(null=False, serialize=True, primary_key=True)
    customer_name = models.CharField(max_length=200)
    customer_surname = models.CharField(max_length=200)
    customer_email = models.CharField(max_length=200)
    products = models.ManyToManyField(Product)
    total_price = models.BigIntegerField()
    additional_info = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + '  ' + str(self.total_price)
