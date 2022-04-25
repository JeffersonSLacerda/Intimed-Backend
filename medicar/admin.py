from django.contrib import admin
from medicar.models import Doctor, Schedule

class Doctors(admin.ModelAdmin):
    list_display = ('id', 'name', 'crm', 'email')
    list_display_link = ('id', 'crm')
    search_fields = ('nome', 'crm', )
    list_per_page = 20
    
admin.site.register(Doctor, Doctors)

class Schedules(admin.ModelAdmin):
    list_display = ('id', 'day', 'hour')
    list_display_link = ('id')
    search_fields = ('day', 'hour', )
    list_per_page = 20
    ordering = 'day', 'hour'
    
admin.site.register(Schedule, Schedules)