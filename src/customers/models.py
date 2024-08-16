from django.db import models

from accounts.models import User

class Customer(User):
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.is_customer = True
        return super(Customer,self).save(*args,**kwargs)