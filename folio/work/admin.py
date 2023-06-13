from django.contrib import admin
from  work.models import *

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("company_name","post_name")
