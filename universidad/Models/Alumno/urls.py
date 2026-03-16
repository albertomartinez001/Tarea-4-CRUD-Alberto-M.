from django.urls import path
from . import views

app_name = 'alumno'

urlpatterns = [
    
    path('', views.alumno_list, name='list'),

    path('nuevo/', views.alumno_create, name='create'),

    path('editar/<int:id>/', views.alumno_update, name='update'),

    path('eliminar/<int:id>/', views.alumno_delete, name='delete'),

    path('cursos/nuevo/', views.curso_create, name='curso_create'),

    path('cursos/editar/<int:id>/', views.curso_update, name='curso_update'),

    path('cursos/eliminar/<int:id>/', views.curso_delete, name='curso_delete'),
    
    path('catedraticos/nuevo/', views.catedratico_create, name='catedratico_create'),

    path('catedraticos/editar/<int:id>/', views.catedratico_update, name='catedratico_update'),

    path('catedraticos/eliminar/<int:id>/', views.catedratico_delete, name='catedratico_delete'),
    path('notas/nuevo/', views.nota_create, name='nota_create'),

    path('notas/editar/<int:id>/', views.nota_update, name='nota_update'),

    path('notas/eliminar/<int:id>/', views.nota_delete, name='nota_delete'),


    path('', views.alumno_list, name='list'),
    path('cursos/', views.curso_list, name='cursos'),
    path('notas/', views.nota_list, name='calificaciones'),
    path('catedraticos/', views.catedratico_list, name='catedraticos'),
    path('asignaciones/', views.asignacion_list, name='asignaciones'),
    path('inscripciones/', views.inscripcion_list, name='inscripciones'),
]