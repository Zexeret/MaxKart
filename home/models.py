from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    query = models.TextField()

    class Meta:
        db_table = "contactus"

    def __str__(self):
        return self.name



class Service(models.Model):
    service_id = models.AutoField
    service_name=models.CharField(max_length=50)
    service_heading = models.CharField(max_length=50)
    service_desc = models.TextField()
    service_icon = models.ImageField(upload_to="home/static/img/service_icons")
    card_heading = models.CharField(max_length=50)

    class Meta:
        db_table = "services"

    def __str__(self):
        return self.service_name


class Haircut(models.Model):
    haircut_id = models.AutoField
    type = models.CharField(max_length=50)
    type_id = models.CharField(max_length=50)
    card_id = models.CharField(max_length=50 , default=" " , blank=True)
    price = models.IntegerField(default=0)
    heading = models.CharField(max_length=100)
    time = models.IntegerField()
    desc = models.TextField()

    class Meta:
        db_table = "Haircut"

    def __str__(self):
        return (self.type + " " + str(self.price) + " " + self.card_id)

    def descaslist(self):
        return self.desc.split(",")


# Dont forget to register it in admin.py