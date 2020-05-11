from django import forms
from .models import Persona, Autor

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido','email']

class AutorForm(forms.ModelForm):
    class Meta:
        model= Autor
        fields= '__all__'