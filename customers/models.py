from django.db import models

class Customers(models.Model):
    TYPE_CHOICES = [
        ('PF', 'Pessoa Física'),
        ('PJ', 'Pessoa Jurídica'),
    ]
    name=models.CharField(max_length=100,null=False,blank=False)
    b_date=models.DateField(null=True,blank=True)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,null=False,blank=False)
    document=models.CharField(max_length=18, null=False,blank=False)
    street = models.CharField(max_length=255,blank=True, null=True)  
    number = models.CharField(max_length=10, blank=True, null=True) 
    neighborhood = models.CharField(max_length=100,blank=True, null=True)  
    city = models.CharField(max_length=100,blank=True, null=True)  
    state = models.CharField(max_length=200,blank=True, null=True) 
    postal_code = models.CharField(max_length=20,blank=True, null=True) 
    observations=models.CharField(max_length=250,blank=True, null=True)
    email = models.EmailField(max_length=40,null=True,blank=True,default='default@example.com')
    phone=models.CharField(max_length=20,null=True,blank=True,default='48999999999')

    def __str__(self):
        return self.name