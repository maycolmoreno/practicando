from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display=('nombre','estado','fecha_creacion')
    resource_class = CategoriaResource

class AutorResource(resources.ModelResource):
    class meta:
        model = Autor
class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display=('nombre','apellido','estado','fecha_creacion')
    resource_class = AutorResource

class PersonaResource(resources.ModelResource):
    class meta:
        model = Persona
class PersonaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display=('nombre','apellido','estado','email')
    resource_class = PersonaResource

admin.site.register(Persona)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Categoria, CategoriaAdmin)

