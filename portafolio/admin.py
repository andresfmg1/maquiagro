from django.contrib import admin
from .models import project

class ProjectAdmin(admin.ModelAdmin): 
     readonly_fields=('created','updated')
admin.site.register(project,ProjectAdmin)