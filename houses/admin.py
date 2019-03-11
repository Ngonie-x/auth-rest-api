from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.HouseModel)
admin.site.register(models.Review)