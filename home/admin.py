from django.contrib import admin
from .models import ContactUs
from .models import Service
from .models import Haircut

admin.site.register(ContactUs)
admin.site.register(Service)
admin.site.register(Haircut)
