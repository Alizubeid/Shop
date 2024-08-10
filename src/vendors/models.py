from django.db import models
from accounts.models import User

class Vendor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    desciption = models.TextField()


