from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(detail)
class detailmaker(admin.ModelAdmin):
    list_display=(
        ['name','age']
    )

    list_filter = [
        "name",
        "age",
        "address",
    ]
    search_fields = ("name",)