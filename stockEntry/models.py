from django.db import models
from products.models import Products
from products.models import Suppliers

class StockEntry(models.Model):
    start_date = models.DateField()
    completion_date = models.DateField(blank=True, null=True)
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE, related_name='stock_entries')
    products = models.ManyToManyField(Products, through='StockEntryProduct', related_name='stock_entries')

class StockEntryProduct(models.Model):
    stock_entry = models.ForeignKey(StockEntry, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
