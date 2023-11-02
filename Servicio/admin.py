from django.contrib import admin
from .models import Servicio

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display=("title","description","price")
    ordering=("title","description")
    search_fields=("title","price")
    readonly_fields=('created','updated')

admin.site.register(Servicio,ProjectAdmin)