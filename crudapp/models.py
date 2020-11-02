from django.db import models

class Customer(models.Model):
    cname = models.CharField(max_length=100)
    cnumber = models.IntegerField()
    cemail = models.EmailField()
    caddress = models.CharField(max_length=10000)
    cservice = models.CharField(max_length=20)
    cprice = models.IntegerField(default=0)
    class Meta:
        db_table = "customer"

