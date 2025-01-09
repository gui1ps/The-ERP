from django.db import models
from products.models import Products
from sales.models import SaleProduct
from django.db.models.signals import post_save
from django.dispatch import receiver

class Stock(models.Model):
    product = models.OneToOneField(Products, on_delete=models.CASCADE, related_name='product')
    quantity = models.PositiveIntegerField(default=0)
    updated_date = models.DateField(auto_now=True)

@receiver(post_save,sender=Products)
def create_stock_for_product(sender, instance, created, **kwargs):
    if created:
        Stock.objects.create(product=instance)

@receiver(post_save,sender=SaleProduct)
def create_stock_for_product(sender, instance, created, **kwargs):
    if created:
        currentStock=Stock.objects.get(product=instance.product)
        if currentStock:
            if currentStock.quantity>=instance.quantity:
                currentStock.quantity-=instance.quantity