from django.contrib import admin

from .models import Realter

class RealterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_mvp', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    seagitrch_fields = ('name',)
    list_editable = ('is_mvp',)

    list_pre_page = 25

admin.site.register(Realter, RealterAdmin)