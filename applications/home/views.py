from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DeleteView, CreateView
from .models import Prueba
from django.urls import reverse_lazy
from .forms import PruebaForm

# Create your views here.

class IndexView(TemplateView):
    template_name = 'home/home.html'


class ResumenFoundationView(TemplateView):
    template_name = 'home/Foundation_css_resumen.html'



class PruebaListView(ListView):
    template_name = 'home/lista.html'
    queryset = ["A","B","C"]
    context_object_name = 'lista_prueba'



class ModeloListView(ListView):
    model = Prueba
    template_name = "home/pruebas.html"
    context_object_name = 'lita_prueba'



class PruebaCreateView(CreateView):
    model = Prueba
    template_name = "home/add.html"
    form_class = PruebaForm
    #success_url = '/sucess' en ves de usar esto, importamos "from django.urls import reverse_lazy"
    success_url = '/'
