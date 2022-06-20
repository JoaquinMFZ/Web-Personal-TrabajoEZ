from django.contrib import admin
from .models import Project

# Register your models here.
class  ProyectAdmin(admin.ModelAdmin):
    readonly_fields = ('create', 'updated')

admin.site.register(Project, ProyectAdmin)