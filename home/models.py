from django.db import models
from django.contrib.auth.models import User

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    query = models.TextField()

    class Meta:
        db_table = "contactus"

    def __str__(self):
        return self.name



class CurrentOrder(models.Model):

    user= models.ForeignKey(User, on_delete=models.CASCADE,default='1')
    service = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    price = models.IntegerField()

    class Meta:
        db_table = "CurrentOrder"

    def __str__(self):
        return str(self.id)

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

class Electrician(models.Model):
    electrician_id = models.AutoField
    type = models.CharField(max_length=50)
    type_id = models.CharField(max_length=50)
    card_id = models.CharField(max_length=50 , default=" " , blank=True)
    price = models.IntegerField(default=0)
    heading = models.CharField(max_length=100)
    time = models.IntegerField()
    desc = models.TextField()

    class Meta:
        db_table = "Electrician"

    def __str__(self):
        return (self.type + " " + str(self.price) + " " + self.card_id)

    def descaslist(self):
        return self.desc.split(",")

class PestControl(models.Model):
    pestControl_id = models.AutoField
    type = models.CharField(max_length=50)
    type_id = models.CharField(max_length=50)
    card_id = models.CharField(max_length=50, default=" ", blank=True)
    price = models.IntegerField(default=0)
    heading = models.CharField(max_length=100)
    time = models.IntegerField()
    desc = models.TextField()

    class Meta:
        db_table = "pestConrol"

    def __str__(self):
        return (self.type + " " + str(self.price) + " " + self.card_id)

    def descaslist(self):
        return self.desc.split(",")

class HouseCleaning(models.Model):
    houseCleaning_id = models.AutoField
    type = models.CharField(max_length=50)
    type_id = models.CharField(max_length=50)
    card_id = models.CharField(max_length=50 , default=" " , blank=True)
    price = models.IntegerField(default=0)
    heading = models.CharField(max_length=100)
    time = models.IntegerField()
    desc = models.TextField()

    class Meta:
        db_table = "houseCleaning"

    def __str__(self):
        return (self.type + " " + str(self.price) + " " + self.card_id)

    def descaslist(self):
        return self.desc.split(",")


class Carpenter(models.Model):
    carpenter_id = models.AutoField
    type = models.CharField(max_length=50)
    type_id = models.CharField(max_length=50)
    card_id = models.CharField(max_length=50 , default=" " , blank=True)
    price = models.IntegerField(default=0)
    heading = models.CharField(max_length=100)
    time = models.IntegerField()
    desc = models.TextField()

    class Meta:
        db_table = "Carpenter"

    def __str__(self):
        return (self.type + " " + str(self.price) + " " + self.card_id)

    def descaslist(self):
        return self.desc.split(",")

class Plumber(models.Model):
    plumber_id = models.AutoField
    type = models.CharField(max_length=50)
    type_id = models.CharField(max_length=50)
    card_id = models.CharField(max_length=50 , default=" " , blank=True)
    price = models.IntegerField(default=0)
    heading = models.CharField(max_length=100)
    time = models.IntegerField()
    desc = models.TextField()

    class Meta:
        db_table = "Plumber"

    def __str__(self):
        return (self.type + " " + str(self.price) + " " + self.card_id)

    def descaslist(self):
        return self.desc.split(",")


class Painter(models.Model):
    painter_id = models.AutoField
    type = models.CharField(max_length=50)
    type_id = models.CharField(max_length=50)
    card_id = models.CharField(max_length=50 , default=" " , blank=True)
    price = models.IntegerField(default=0)
    heading = models.CharField(max_length=100)
    time = models.IntegerField()
    desc = models.TextField()

    class Meta:
        db_table = "Painter"

    def __str__(self):
        return (self.type + " " + str(self.price) + " " + self.card_id)

    def descaslist(self):
        return self.desc.split(",")


class Salon(models.Model):
    salon_id = models.AutoField
    type = models.CharField(max_length=50)
    type_id = models.CharField(max_length=50)
    card_id = models.CharField(max_length=50 , default=" " , blank=True)
    price = models.IntegerField(default=0)
    heading = models.CharField(max_length=100)
    time = models.IntegerField()
    desc = models.TextField()

    class Meta:
        db_table = "Salon"

    def __str__(self):
        return (self.type + " " + str(self.price) + " " + self.card_id)

    def descaslist(self):
        return self.desc.split(",")

class Profile(models.Model):
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    phone=models.CharField(max_length=15,default="")
    address=models.CharField(max_length=150)
    city=models.CharField(max_length=70)
    state=models.CharField(max_length=70)
    pincode=models.CharField(max_length=7)

    class Meta:
        db_table = "profile"

    def __str__(self):
        return (self.user.first_name)

# address
# city
# state
# pincode
# Dont forget to register it in admin.py