from django.urls import path
from . import views

urlpatterns = [

    path('new-departamento/', views.NewDepartamenView.as_view(),name="new_departamento"),



]