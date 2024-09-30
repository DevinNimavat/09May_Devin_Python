from django.contrib import admin
from .models import *

# Register your models here.

class insuranceAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['fnm','lnm','em','unm','mobile','dob']

class healthdata_Admin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['fullnm','em','mobile','type']

class lifedata_Admin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['fullnm','em','mobile','type']

class vehicledata_Admin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['fullnm','em','mobile','type']

class homedata_Admin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['fullnm','em','mobile','type']

class traveldata_Admin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['fullnm','em','mobile','type']

class businessdata_Admin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['fullnm','business_em','owner_no','type','gts_no']


admin.site.register(insurance,insuranceAdmin)
admin.site.register(healthdata,healthdata_Admin)
admin.site.register(lifedata,lifedata_Admin)
admin.site.register(vehicledata,vehicledata_Admin)
admin.site.register(homedata,homedata_Admin)
admin.site.register(traveldata,traveldata_Admin)
admin.site.register(businessdata,businessdata_Admin)

