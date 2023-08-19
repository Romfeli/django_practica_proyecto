from django.urls import path
from . import views

app_name = 'departamento_app'

urlpatterns = [

    path('lista_departamento/', views.DepartamentoListView.as_view(),name="lista_departamento"),


    path('new-departamento/', views.NewDepartamenView.as_view(),name="new_departamento"),





]