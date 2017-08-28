from django.contrib import admin
from .models import (
    Drink,
    Data
)

# Register your models here.
admin.site.register(Drink)
admin.site.register(Data)
