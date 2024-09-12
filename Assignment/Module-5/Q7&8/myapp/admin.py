from django.contrib import admin
from .models import *

# Register your models here.
class productdetails(admin.ModelAdmin):
    
    list_display=['pname','price','img','ram','pmodel']
    
admin .site.register(product_master)
admin.site.register(sub_cate)