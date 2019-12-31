from django.db import models


class Product(models.Model):
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
