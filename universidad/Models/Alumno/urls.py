from django.urls import path
from . import views

app_name = 'alumno'

urlpatterns = [
    path('', views.alumno_list, name='list'),
    path('cursos/', views.curso_list, name='cursos'),
    path('notas/', views.nota_list, name='calificaciones'),
    path('catedraticos/', views.catedratico_list, name='catedraticos'),
    path('asignaciones/', views.asignacion_list, name='asignaciones'),
    path('inscripciones/', views.inscripcion_list, name='inscripciones'),
]