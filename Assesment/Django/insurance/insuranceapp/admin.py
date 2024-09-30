from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(insurance)
admin.site.register(healthdata)
admin.site.register(lifedata)
admin.site.register(vehicledata)
admin.site.register(homedata)
admin.site.register(traveldata)
admin.site.register(businessdata)

