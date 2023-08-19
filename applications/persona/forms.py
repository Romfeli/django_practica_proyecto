from django import forms

from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    """Form definition for empleado."""

    class Meta:
        """Meta definition for empleadoform."""

        model = Empleado
        fields = ('first_name',
                  'last_name',
                  'full_name',
                  'job',
                  'departamento',
                  'avatar',
                   'habilidades',
                  )
        
        widgets = {
            'habilidades':forms.CheckboxSelectMultiple()

        }
        

