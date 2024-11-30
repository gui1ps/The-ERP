from django.db import models
from products.models import Products

class Stock(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='stocks')
    quantity = models.PositiveIntegerField()
    updated_date = models.DateField(auto_now=True)
