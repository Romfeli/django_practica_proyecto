from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento
# Create your views here.


class NewDepartamenView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        #logiica
        print('estamos en el form valid')

        #creamops una intancia para con los datos recuperadospara ser utilizado en la creacion del empleado
        depa= Departamento(
            name=form.cleaned_data['departamento'],
            short_name=form.cleaned_data['short_name_departamento']

        )
        depa.save()


        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']

        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento = depa

        )

        return super(NewDepartamenView, self).form_valid(form)
