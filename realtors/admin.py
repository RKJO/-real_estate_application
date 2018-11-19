from django.contrib import admin

from .models import Realter

class RealterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    seagitrch_fields = ('name',)
    list_pre_page = 25

admin.site.register(Realter, RealterAdmin)