from django.urls import path
from . import views

# le damos un nombre a todas las urls
app_name = 'persona_app'

urlpatterns = [
    #list views
    path('listar-todo-empleado/', views.ListAllEmpleados.as_view()),
    path('listar-by-area/<short_name>', views.ListByArea.as_view()),
    path('listar-by-work/<job>', views.ListByWork.as_view()),
    path('listar-by-kword/', views.ListarEmpleadoPorPalabraClave.as_view()),
    path('listar-by-habilidades/', views.ListHabilidadesEmpleados.as_view()),


    #details view
    path('ver-empleado/<pk>', views.EmpleadoDetailView.as_view()),
    #create view
    path('add_empleado/', views.EmpleadoCreateView.as_view()),
    #                                                  le etiqueda name nos da la oportunidad de referirnos a esta url mediante el resver_lazy
    path('sucess/', views.SusscessView.as_view(), name='correcto' ),
    #update view
    path('update/<pk>', views.EmpleadoUpdateView.as_view(), name='update' ),
    #deleteview
    path('delete/<pk>', views.EmpleadoDeleteView.as_view(), name='delete' ),





   


]