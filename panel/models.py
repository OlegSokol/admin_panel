from django.db import models
from django.utils import timezone

class Product(models.Model):
    product_number = models.BigIntegerField(null=False, serialize=True)
    description = models.CharField(max_length=200)
    image_id = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    price = models.BigIntegerField()
