from django.db import models


class Cart(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_quantity = models.PositiveIntegerField()
