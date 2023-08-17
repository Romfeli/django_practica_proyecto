from django import forms
from .models import Prueba

class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        fields = ['titulo',
              'subtitulo',
              'cantidad',
              ]
        

        widgets = {
            'titulo': forms.TextInput(
                attrs= {
                    'placeholder':'ingrese el titulo aqui'
                }
            ),
            'subtitulo': forms.TextInput(
                attrs= {
                    'placeholder':'ingrese el subtitulo aqui'
                }
            ),
            'cantidad': forms.TextInput(
                attrs= {
                    'placeholder':'ingrese un numero aqui'
                }
            )
        }




        #sobre escribimos el metodo de que modifica la cantidad recibida por el formulario
    def clean_cantidad(self):
        #de esta forma recuperamos el valor introducido en el formulario
        cantidad = self.cleaned_data['cantidad']
        #logica de la validacion
        if cantidad < 10:
            #levantamos un error si no se cumple
            raise forms.ValidationError('Ingrese un numero valor a 10')
        return cantidad

            
