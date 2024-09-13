from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(detail)
class detailmaker(admin.ModelAdmin):
    list_display=(
        ['name','age']          #this will display name and age of data in admin pannel
    )

    list_filter = [             
        "name",             #this will create a filter in admin pannel
        "age",
        "address",
    ]
    search_fields = ("name",)           #create a search bar for name in admin pannel