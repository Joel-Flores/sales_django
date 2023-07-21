from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.ProductName)
admin.site.register(models.ProductType)