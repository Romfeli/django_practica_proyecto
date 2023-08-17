from django.contrib import admin
#importamos el modelo que anterior mente creamos 
from .models import Departamento
# Register your models here.
#creamos este comando escribiendo el autoompletar de register, y ponermos el modelo creado
admin.site.register(Departamento)