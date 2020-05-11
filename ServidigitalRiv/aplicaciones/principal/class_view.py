from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from .forms import PersonaForm, AutorForm
from .models import Persona, Autor

class PersonaList(ListView):
    queryset= Persona.objects.filter(estado=True)
    template_name='index.html'

class PersonaCreate(CreateView):
    model= Persona
    form_class= PersonaForm
    template_name= 'crear_persona.html'
    success_url = reverse_lazy('index')

class PersonaUpdate(UpdateView):
    model= Persona
    form_class= PersonaForm
    template_name= 'crear_persona.html'
    success_url = reverse_lazy('index')

class PersonaDelete(DeleteView):
    model= Persona
    template_name= 'vericacion.html'
    success_url = reverse_lazy('index')

class AutorCreate(CreateView):
    model= Autor
    form_class= AutorForm
    template_name= 'crear_persona.html'
    success_url = reverse_lazy('index')

class AutorList(ListView):
    queryset= Autor.objects.filter(estado=True)
    template_name='autor.html'