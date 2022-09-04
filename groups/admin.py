from django.contrib import admin
from groups.models import Groups


@admin.register(Groups)
class Groups_admin(admin.ModelAdmin):
    list_display= ["type", "team1","team2","team3","team4",]

