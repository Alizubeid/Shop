from django.db import models
from customers.models import Customer
from cart.models import Product

class Comment(models.Model):
    SCORE = (
        ("0","0"),
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
    )
    comment = models.TextField()
    score = models.CharField(max_length=4,choices=SCORE,default="0")
    customer = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product,on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name =  "کامنت"
        verbose_name_plural = "کامنت ها"
