from django.db import models

class Suppliers(models.Model):
    name = models.CharField(max_length=100)
    phone=models.CharField(max_length=20,null=False,blank=False,default='48999999999')
    email = models.EmailField(max_length=40,null=False,blank=False,default='default@example.com')
    document=models.CharField(max_length=18, null=False,blank=False)
    observations=models.CharField(max_length=250,blank=True, null=True)
    street = models.CharField(max_length=255,blank=True, null=True)  
    number = models.CharField(max_length=10, blank=True, null=True) 
    neighborhood = models.CharField(max_length=100,blank=True, null=True)  
    city = models.CharField(max_length=100,blank=True, null=True)  
    state = models.CharField(max_length=2,blank=True, null=True) 
    postal_code = models.CharField(max_length=20,blank=True, null=True) 


