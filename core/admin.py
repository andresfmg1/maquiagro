from django.contrib import admin

# Register your models here.
from .models import iconos,category,pagina



class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')
admin.site.register(iconos,ProjectAdmin)

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')


admin.site.register(category,CategoryAdmin)

class ProjectAdmin(admin.ModelAdmin):
    readonly_fields=('created','update')
admin.site.register(pagina,ProjectAdmin)