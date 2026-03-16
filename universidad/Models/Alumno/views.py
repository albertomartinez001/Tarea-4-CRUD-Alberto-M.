from django.shortcuts import render, redirect, get_object_or_404

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
    return render(
        request,
        'alumno/alumno/list.html',
        {'alumnos': alumnos}
    )
    
def alumno_create(request):

    if request.method == "POST":

        Alumno.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            gender=request.POST['gender'],
            birth_date=request.POST['birth_date'],
            is_active=request.POST.get('is_active') == 'on'
        )

        return redirect('alumno:list')

    return render(request, 'alumno/alumno/create.html')

def alumno_update(request, id):
    alumno = get_object_or_404(Alumno, id=id)

    if request.method == "POST":
        alumno.first_name = request.POST['first_name']
        alumno.last_name = request.POST['last_name']
        alumno.email = request.POST['email']
        alumno.phone = request.POST['phone']
        alumno.gender = request.POST['gender']
        alumno.birth_date = request.POST['birth_date']
        alumno.is_active = request.POST.get('is_active') == 'on'
        alumno.save()
        return redirect('alumno:list')

    return render(request, 'alumno/alumno/update.html', {'alumno': alumno})

def alumno_delete(request, id):
    alumno = get_object_or_404(Alumno, id=id)
    if request.method == "POST":
        alumno.delete()
        return redirect('alumno:list')
    return render(request, 'alumno/alumno/delete.html', {'alumno': alumno})

def curso_list(request):
    cursos = Curso.objects.all()
    return render(request, 'alumno/cursos/list.html', {'cursos': cursos})

def curso_create(request):

    if request.method == "POST":

        Curso.objects.create(
            nombre=request.POST['nombre'],
            descripcion=request.POST['descripcion']
        )

        return redirect('alumno:cursos')

    return render(request, 'alumno/cursos/create.html')

def curso_update(request, id):

    curso = get_object_or_404(Curso, id=id)

    if request.method == "POST":

        curso.nombre = request.POST['nombre']
        curso.descripcion = request.POST['descripcion']

        curso.save()

        return redirect('alumno:cursos')

    return render(request, 'alumno/cursos/update.html', {'curso': curso})


def curso_delete(request, id):

    curso = get_object_or_404(Curso, id=id)

    if request.method == "POST":

        curso.delete()

        return redirect('alumno:cursos')

    return render(request, 'alumno/cursos/delete.html', {'curso': curso})


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