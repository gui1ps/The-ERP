from django.db import models

class Notes(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=500)
    #created_at=models.DateField(auto_now=True)
    #updated_at=models.DateField(auto_now=True)