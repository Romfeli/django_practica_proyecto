from django import forms
#creamos el formulario de esta manera

class NewDepartamentoForm(forms.Form):
    #usamos el plugin para cf para hacer los campos de charfield
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    departamento = forms.CharField(max_length=50)
    short_name_departamento = forms.CharField(max_length=20)