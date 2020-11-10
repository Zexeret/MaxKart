from django.contrib import admin
from .models import ContactUs
from .models import Service
from .models import Haircut
from .models import CurrentOrder

admin.site.register(ContactUs)
admin.site.register(Service)
admin.site.register(Haircut)
admin.site.register(CurrentOrder)

