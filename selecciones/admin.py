from django.contrib import admin
from selecciones.models import Selecciones


@admin.register(Selecciones)
class Selecciones_admin(admin.ModelAdmin):
    list_display= ["name", "federation"]



