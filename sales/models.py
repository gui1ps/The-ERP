from django.db import models
from products.models import Products
from customers.models import Customers

class Payment_Method(models.Model):
    name=models.CharField(max_length=200,null=False,blank=False)
    def __str__(self):
        return self.name
    
class Sale(models.Model):
    paymentmethod=models.ForeignKey(Payment_Method,on_delete=models.CASCADE,related_name='forma_pagamento')
    customer=models.ForeignKey(Customers,on_delete=models.CASCADE,related_name='clientes')
    total=models.PositiveIntegerField(default=0)
    crated_date=models.DateField(auto_now=True)

class SaleProduct(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="sale_products")
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="sale_products")
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)