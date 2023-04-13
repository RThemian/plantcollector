from django.contrib import admin
from .models import Watering, Plant, Photo, Pollinator
# Register your models here.

admin.site.register([Watering, Plant, Photo, Pollinator])