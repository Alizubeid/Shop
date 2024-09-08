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
    image = models.ImageField(upload_to=f"shops/images/{company_name}/")
    def __str__(self):
        return f"{self.company_name}"
    
    class Meta:
        verbose_name = "شرکت"
        verbose_name_plural = "شرکت"


class Companies(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=64,null=True)
    is_main = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.company} {'MAIN' if self.is_main else ''}"
    class Meta:
        verbose_name = "زیرمجموعه"
        verbose_name_plural = "شرکت هایه زیرمحموعه"

class Staff(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_manager = models.BooleanField(default=False)
    is_operator = models.BooleanField(default=False)
    company = models.ForeignKey(Companies,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return f"{self.user} {'manager' if self.is_manager else 'operator' }"
    class Meta:
        verbose_name = "کارمند"
        verbose_name_plural = "کارمندان"
    def save(self, *args, **kwargs):
        self.user.is_staff = True
        return super(Staff, self).save(*args, **kwargs)

class Manager(Staff):
    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        self.is_manager = True
        return super(Manager, self).save(*args, **kwargs)

class Operator(Staff):
    class Meta:
        proxy = True
    
    def save(self, *args, **kwargs):
        self.is_operator = True
        return super(Operator, self).save(*args, **kwargs)