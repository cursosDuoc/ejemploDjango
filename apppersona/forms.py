from django import forms

from .models import Persona

class FormularioPersona(forms.ModelForm):
    """
    Esta clase representa un formulario para una persona
    La magia ocurre porque heredamos de ModelForm
    """
    class Meta :
        model = Persona # clase base para este formulario
        fields = ('nombre', 'apellido', 'rut')
