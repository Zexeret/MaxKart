from django.contrib import admin
from .models import ContactUs
from .models import Service
from .models import Haircut
from .models import CurrentOrder
from .models import Electrician
from .models import PestControl
from .models import HouseCleaning
from .models import Carpenter
from .models import Plumber
from .models import Painter
from .models import Salon
from .models import Profile


admin.site.register(ContactUs)
admin.site.register(CurrentOrder)
admin.site.register(Service)
admin.site.register(Haircut)
admin.site.register(Salon)
admin.site.register(Painter)
admin.site.register(Plumber)
admin.site.register(Carpenter)
admin.site.register(HouseCleaning)
admin.site.register(PestControl)
admin.site.register(Electrician)
admin.site.register(Profile)






