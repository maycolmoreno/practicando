
from django.urls import path
from ServidigitalRiv.aplicaciones.principal.views import *
from ServidigitalRiv.aplicaciones.principal.class_view import *
urlpatterns = [
    path('', home, name='index'),
    path('acerca', acerca, name='acerca'),
    path('contacto', contacto, name='contacto'),
    path('login', login, name='login'),
    path('menu', menu, name='menu'),
    path('register', register, name='register'),
    path('single', single, name='single'),


    #path('', PersonaList.as_view(), name = 'index'), 
    path('crearpersona',PersonaCreate.as_view(), name = 'crear_persona'),
    path('editar_persona/<int:pk>/',PersonaUpdate.as_view(), name='editarPersona'),
    path('eliminar_persona/<int:pk>/',PersonaDelete.as_view(), name='eliminarPersona'),
    path('crearautor',AutorCreate.as_view(), name = 'crearautor'),
    path('autor', AutorList.as_view(), name = 'autor'),
]
