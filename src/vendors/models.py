from django.db import models
from accounts.models import User, Address


class Owner(User):
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.is_owner = True
        return super(Owner, self).save(*args, **kwargs)


class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    desciption = models.TextField()


