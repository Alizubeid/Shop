from django.db import models
from accounts.models import User, Address


class Owner(User):
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.is_owner = True
        self.is_staff = True
        return super(Owner, self).save(*args, **kwargs)


class Company(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.DO_NOTHING)
    company_name = models.CharField(max_length=255,unique=True)
    images = models.ImageField("company/%y/%m/%d")
    desciption = models.TextField()
    def __str__(self):
        return self.company_name

class Companies(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=64)
    is_main = models.BooleanField(default=False)
    descripton = models.TextField()
    def __str__(self):
        return self.company

class Staff(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_manager = models.BooleanField(default=False)
    is_operator = models.BooleanField(default=False)
    company = models.ForeignKey(Companies,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.user.email

class Manager(Staff):
    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        self.is_manager = True
        self.user.is_staff = True
        return super(Manager, self).save(*args, **kwargs)

class Operator(Staff):
    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        self.is_operator = True
        self.user.is_staff = True
        return super(Operator, self).save(*args, **kwargs)