from django.db import models
from vendors.models import Company

class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.PositiveIntegerField()
    date_pd = models.DateField()
    date_ex = models.DateField()
    company = models.ForeignKey(Company,on_delete=models.CASCADE)


