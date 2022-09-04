from django.contrib import admin
from plantel.models import Plantel


@admin.register(Plantel)
class Plantel_admin(admin.ModelAdmin):
    list_display= ["full_name", "height", "age", "club", "position"]