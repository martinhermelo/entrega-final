from django.contrib import admin
from estadios.models import Estadios


@admin.register(Estadios)
class Estadios_admin(admin.ModelAdmin):
    list_display= ["name", "image"]