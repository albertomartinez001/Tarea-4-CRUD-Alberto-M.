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
    return render(request, 'alumno/notas/list.html', {'notas': notas})

def nota_create(request):

    alumnos = Alumno.objects.all()
    asignaciones = AsignacionCurso.objects.all()

    if request.method == "POST":

        Notas.objects.create(
            alumno_id=request.POST['alumno'],
            asignacion_id=request.POST['asignacion'],
            nota=request.POST['nota']
        )

        return redirect('alumno:calificaciones')

    return render(request, 'alumno/notas/create.html', {
        'alumnos': alumnos,
        'asignaciones': asignaciones
    })


def nota_delete(request, id):

    nota = get_object_or_404(Notas, id=id)

    if request.method == "POST":

        nota.delete()

        return redirect('alumno:calificaciones')

    return render(request, 'alumno/notas/delete.html', {'nota': nota})


def nota_update(request, id):

    nota = get_object_or_404(Notas, id=id)

    alumnos = Alumno.objects.all()
    asignaciones = AsignacionCurso.objects.all()

    if request.method == "POST":

        nota.alumno_id = request.POST['alumno']
        nota.asignacion_id = request.POST['asignacion']
        nota.nota = request.POST['nota']

        nota.save()

        return redirect('alumno:calificaciones')

    return render(request, 'alumno/notas/update.html', {
        'nota': nota,
        'alumnos': alumnos,
        'asignaciones': asignaciones
    })


def catedratico_list(request):
    catedraticos = Catedratico.objects.all()
    return render(request, 'alumno/catedraticos/list.html', {'catedraticos': catedraticos})

def catedratico_create(request):

    if request.method == "POST":

        Catedratico.objects.create(
            nombre=request.POST['nombre'],
            email=request.POST['email']
        )

        return redirect('alumno:catedraticos')

    return render(request, 'alumno/catedraticos/create.html')

def catedratico_update(request, id):

    catedratico = get_object_or_404(Catedratico, id=id)

    if request.method == "POST":

        catedratico.nombre = request.POST['nombre']
        catedratico.email = request.POST['email']

        catedratico.save()

        return redirect('alumno:catedraticos')

    return render(request, 'alumno/catedraticos/update.html', {'catedratico': catedratico})



def catedratico_delete(request, id):

    catedratico = get_object_or_404(Catedratico, id=id)

    if request.method == "POST":

        catedratico.delete()

        return redirect('alumno:catedraticos')

    return render(request, 'alumno/catedraticos/delete.html', {'catedratico': catedratico})

def asignacion_list(request):
    asignaciones = AsignacionCurso.objects.all()
    return render(request, 'alumno/asignacion_cursos/list.html', {
        'asignaciones': asignaciones
    })
    
def asignacion_create(request):

    cursos = Curso.objects.all()
    catedraticos = Catedratico.objects.all()

    if request.method == "POST":

        AsignacionCurso.objects.create(
            curso_id=request.POST['curso'],
            catedratico_id=request.POST['catedratico'],
            horario=request.POST['horario']
        )

        return redirect('alumno:asignaciones')

    return render(request, 'alumno/asignacion_cursos/create.html', {
        'cursos': cursos,
        'catedraticos': catedraticos
    })

def asignacion_update(request, id):

    asignacion = get_object_or_404(AsignacionCurso, id=id)

    cursos = Curso.objects.all()
    catedraticos = Catedratico.objects.all()

    if request.method == "POST":

        asignacion.curso_id = request.POST['curso']
        asignacion.catedratico_id = request.POST['catedratico']
        asignacion.horario = request.POST['horario']

        asignacion.save()

        return redirect('alumno:asignaciones')

    return render(request, 'alumno/asignacion_cursos/update.html', {
        'asignacion': asignacion,
        'cursos': cursos,
        'catedraticos': catedraticos
    })

def asignacion_delete(request, id):

    asignacion = get_object_or_404(AsignacionCurso, id=id)

    if request.method == "POST":

        asignacion.delete()

        return redirect('alumno:asignaciones')

    return render(request, 'alumno/asignacion_cursos/delete.html', {
        'asignacion': asignacion
    })

def inscripcion_list(request):
    inscripciones = InscripcionAlumno.objects.all()

    return render(request, 'alumno/inscripcion/list.html', {
        'inscripciones': inscripciones
    })


def inscripcion_create(request):

    alumnos = Alumno.objects.all()
    asignaciones = AsignacionCurso.objects.all()

    if request.method == "POST":

        InscripcionAlumno.objects.create(
            alumno_id=request.POST['alumno'],
            asignacion_id=request.POST['asignacion'],
            fecha_inscripcion=request.POST['fecha_inscripcion']
        )

        return redirect('alumno:inscripciones')

    return render(request, 'alumno/inscripcion/create.html', {
        'alumnos': alumnos,
        'asignaciones': asignaciones
    })


def inscripcion_update(request, id):

    inscripcion = get_object_or_404(InscripcionAlumno, id=id)

    alumnos = Alumno.objects.all()
    asignaciones = AsignacionCurso.objects.all()
    

    if request.method == "POST":

        inscripcion.alumno_id = request.POST['alumno']
        inscripcion.asignacion_id = request.POST['asignacion']
        inscripcion.save()

        return redirect('alumno:inscripciones')

    return render(request, 'alumno/inscripcion/update.html', {
        'inscripcion': inscripcion,
        'alumnos': alumnos,
        'asignaciones': asignaciones
    })


def inscripcion_delete(request, id):

    inscripcion = get_object_or_404(InscripcionAlumno, id=id)

    if request.method == "POST":
        inscripcion.delete()
        return redirect('alumno:inscripciones')

    return render(request, 'alumno/inscripcion/delete.html', {
        'inscripcion': inscripcion
    })
