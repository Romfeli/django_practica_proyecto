from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .models import Empleado
from django.urls import reverse_lazy
from .forms import EmpleadoForm

# Create your views here.


class InicioView(TemplateView):
    template_name = "inicio.html"



#requiere de un template html
class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 4
    ordering = 'first_name'
    context_object_name = 'empleados'

    def get_queryset(self):
                                        #vvvvv este parametro tiene que ser el mismo informado en el input
        palabra_clave = self.request.GET.get("kword", '')
        ##creamos una lista filtrada donde la palabra clave recogida por le metodo get tiene que ser igual al atributo en la base de datos
        lista = Empleado.objects.filter(
            first_name__icontains=palabra_clave
        ) 

        return lista


#requiere de un template html
class ListAllEmpleadosAdmin(ListView):
    model = Empleado    
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = 'first_name'
    context_object_name = 'empleados'



 #requiere de un template html
class ListByArea(ListView):
 #lista empleados de area en especifico
    template_name = 'persona/list_by_area.html'
    context_object_name ="empleados"
 
    # metodo para hacer listado de forma dinamica
    def get_queryset(self):
        #kwargs recupera del url lo que se estan mandando
        area = self.kwargs['short_name']
        #creamos un filtro interactuando con el navegador
        lista = Empleado.objects.filter(
        departamento__short_name = area
 ) 
        return lista




class ListByWork(ListView):
 #lista empleados de area en especifico
    template_name = 'persona/list_by_work.html'
 
    # metodo para hacer listado de forma dinamica
    def get_queryset(self):
        #kwargs recupera del url lo que se estan mandando
        area = self.kwargs['job']
        #creamos un filtro interactuando con el navegador
        lista = Empleado.objects.filter(job__name=area) 
        return lista
    



class ListarEmpleadoPorPalabraClave(ListView):
 #lista empleados por palabra clave
    template_name = 'persona/list_by_kword.html'
    context_object_name = 'empleado'


    # metodo para hacer listado de forma dinamica
    def get_queryset(self):
        print('************')
                                            #vvvvv este parametro tiene que ser el mismo informado en el input
        palabra_clave = self.request.GET.get("kword", '')
        ##creamos una lista filtrada donde la palabra clave recogida por le metodo get tiene que ser igual al atributo en la base de datos
        lista = Empleado.objects.filter(first_name=palabra_clave) 
        print(lista)
        return lista
    

class ListHabilidadesEmpleados(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        #al utilizar el orm de django vvv recuperamos un unico registro de la base de datos
        id_empleado = self.request.GET.get("nombre", '')
        empleado = Empleado.objects.get(id=id_empleado)
        
        return empleado.habilidades.all()
    



class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    # de esta forma intervenimos metodos
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        #podemos agregar variagles desde aqui
        context['titulo'] = 'empleado del mes'
        return context
    


class SusscessView(TemplateView):
    template_name = "persona/sucess.html"




#necesita de 4 campos para funcionar el create iew
class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"

    #fields = ('__all__') de esta forma jalamos todos los datos del modelo de la base de datos
    form_class = EmpleadoForm
    #success_url = '/sucess' en ves de usar esto, importamos "from django.urls import reverse_lazy"
    success_url = reverse_lazy('persona_app:empleados_admin')


    ## es una forma de interseptar el from valid
    def form_valid(self, form):
        #logica del proceso
        # recoje todos los datos enviados en el formulario y los guarda ene sta variable empleado
        empleado = form.save()
        # de esta forma agregarmos el full name al registro de la base de datos
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        print(empleado)

        # el super v v se utiliza para sobre escribir un metodo de la class EmpleadoCreateView
        return super(EmpleadoCreateView, self).form_valid(form)



class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    fields = ['first_name',
              'last_name',
              'job',
              'departamento',
              'habilidades',
              ]
    success_url = reverse_lazy('persona_app:empleados_admin')


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('****** METHOD POSTTT*********')
        print('***************')
        print(request.POST)
        print(request.POST['last_name'])

        return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        #logica del proceso
        print('****** METHOD FORM VALID*********')
        print('***************')
        print('***************')
           # el super v v se utiliza para sobre escribir un metodo de la class EmpleadoCreateView
        return super(EmpleadoUpdateView, self).form_valid(form)



class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete.html"
    success_url = reverse_lazy('persona_app:empleados_admin')

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
