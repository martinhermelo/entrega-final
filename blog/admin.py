from django.contrib import admin
from blog.models import Notes


@admin.register(Notes)
class Notes_admin(admin.ModelAdmin):
    list_display= ["title","description",  "author", "email", ]

