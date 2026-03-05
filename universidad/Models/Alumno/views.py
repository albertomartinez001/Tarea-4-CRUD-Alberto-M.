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
    return render(request, 'curso/list.html', {'cursos': cursos})

def nota_list(request):
    notas = Notas.objects.all()
    return render(request, 'nota/list.html', {'notas': notas})

def catedratico_list(request):
    catedraticos = Catedratico.objects.all()
    return render(request, 'catedratico/list.html', {'catedraticos': catedraticos})

def asignacion_list(request):
    asignaciones = AsignacionCurso.objects.all()
    return render(request, 'asignacion/list.html', {'asignaciones': asignaciones})

def inscripcion_list(request):
    inscripciones = InscripcionAlumno.objects.all()
    return render(request, 'inscripcion/list.html', {'inscripciones': inscripciones})