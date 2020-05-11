"""ServidigitalRiv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ServidigitalRiv.aplicaciones.principal.views import *
from ServidigitalRiv.aplicaciones.principal.class_view import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PersonaList.as_view(), name = 'index'),
    path('crearpersona',PersonaCreate.as_view(), name = 'crear_persona'),
    path('editar_persona/<int:pk>/',PersonaUpdate.as_view(), name='editarPersona'),
    path('eliminar_persona/<int:pk>/',PersonaDelete.as_view(), name='eliminarPersona'),
    path('crearautor',AutorCreate.as_view(), name = 'crearautor'),
    path('autor', AutorList.as_view(), name = 'autor'),


    

]
