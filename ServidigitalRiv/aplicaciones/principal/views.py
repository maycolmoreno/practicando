from django.shortcuts import render, redirect
from .models import *
from .forms import PersonaForm, AutorForm

def home(request):
    return render(request,'index.html')
#     autor= Autor.objects.all()
#     contexto = {
#         'autor':autor
#     }
#     return render(request,'index.html')

def acerca(request):
    return render(request,'about.html')

def contacto(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

def menu(request):
    return render(request,'menu.html')

def register(request):
    return render(request,'register.html')

def single(request):
    return render(request,'single.html')
# def crearAutor(request):
#     if request.method=='POST':
#         form= AutorForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#         else:
#             form= AutorForm
#             contexto={
#                 'form':form
#             }
#             return render(request,'crear_persona.html', contexto)

# def crearPersona(request):
#     if request.method == 'GET':
#         form = PersonaForm()
#         contexto = {
#             'form': form
#         }
#     else:
#         form = PersonaForm(request.POST)
#         contexto = {
#             'form': form
#         }
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     return render(request,'crear_persona.html', contexto)

# def editarPersona(request,id):
#     persona = Persona.objects.get(id = id)
#     if request.method == 'GET':
#         form = PersonaForm(instance = persona)
#         contexto = {
#             'form':form
#         }
#     else:
#         form = PersonaForm(request.POST, instance = persona)
#         contexto = {
#             'form':form
#         }
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     return render(request,'crear_persona.html', contexto)

# def eliminarPersona(request, id):
#     persona = Persona.objects.get(id=id)
#     persona.delete()
#     return redirect('index')