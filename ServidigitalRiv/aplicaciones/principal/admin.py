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

class PostResource(resources.ModelResource):
    class meta:
        model =Post

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo']
    list_display=('titulo','slug','autor','imagen')
    resource_class = PostResource

class LibroResource(resources.ModelResource):
    class meta:
        model =Libro

class LibroAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo', 'fecha_creacion']
    list_display=('titulo','fecha_creacion')
    resource_class = LibroResource

admin.site.register(Persona, PersonaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Libro, LibroAdmin)
