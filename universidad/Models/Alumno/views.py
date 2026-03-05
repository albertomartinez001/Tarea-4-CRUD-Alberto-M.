from django.shortcuts import render
from .models import (
    Alumno,
    Curso,
    Notas,
    Catedratico,
    AsignacionCurso,
    InscripcionAlumno
)

def alumno_list(request):
    alumnos = Alumno.objects.all()
    return render(request, 'alumno/list.html', {'alumnos': alumnos})

def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'alumno/cursos.html', {'cursos': cursos})

def nota_list(request):
    notas = Notas.objects.all()
    return render(request, 'alumno/calificaciones.html', {'notas': notas})

def catedratico_list(request):
    catedraticos = Catedratico.objects.all()
    return render(request, 'alumno/catedraticos.html', {'catedraticos': catedraticos})

def asignacion_list(request):
    asignaciones = AsignacionCurso.objects.all()
    return render(request, 'alumno/asignaciones.html', {'asignaciones': asignaciones})

def inscripcion_list(request):
    inscripciones = InscripcionAlumno.objects.all()
    return render(request, 'alumno/inscripciones.html', {'inscripciones': inscripciones})