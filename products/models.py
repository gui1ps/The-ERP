from django.db import models
from suppliers.models import Suppliers

class Units(models.Model):
    name=models.CharField(max_length=10,null=False,blank=False)
    description=models.CharField(max_length=250,null=False,blank=False)
    def __str__(self):
        return self.name

class Products(models.Model):
    name=models.CharField(max_length=100,null=False,blank=False)
    reference=models.CharField(max_length=10,null=False,blank=False)
    fornecedores = models.ManyToManyField(Suppliers, related_name='produtos')
    unit = models.ForeignKey(Units, on_delete=models.CASCADE, related_name='products')    
    local=models.CharField(max_length=25,null=False,blank=False)
    p_cost=models.FloatField(null=False,blank=False)
    p_sell=models.FloatField(null=False,blank=False)
    profit=models.FloatField(null=False,blank=False)

    def __str__(self):
        return self.name

