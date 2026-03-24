from django.core.management.base import BaseCommand
from universidad.Models.Alumno.models import Alumno
from datetime import date
import random

class Command(BaseCommand):
    help = 'Puebla la tabla Alumno con 10,000 registros de prueba'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.HTTP_INFO("Iniciando la creación de 10,000 alumnos..."))
        
        generos = ['M', 'F']
        alumnos_lista = []

        for i in range(10000):
            # Creamos el objeto en memoria basado en nuestro modelo creado desde la tarea anterior
            nuevo_alumno = Alumno(
                first_name=f"Nombre_{i}",
                last_name=f"Apellido_{i}",
                email=f"alumno.test.{i}@universidad.edu",
                phone=f"1234{i:04d}", # Genera un número de relleno para mantener mi formato
                gender=random.choice(generos),
                birth_date=date(2000, 1, 1), # Fecha fija para simplificar y evitar problemas si se quiere validar despues 
                is_active=True
            )
            alumnos_lista.append(nuevo_alumno)

        # Usamos bulk_create para insertar todo en una sola ejecución SQL
        # Esto es 100 veces más rápido que hacer .save() en cada vuelta del loop
        try:
            Alumno.objects.bulk_create(alumnos_lista, batch_size=500)
            self.stdout.write(self.style.SUCCESS(f'¡Éxito! Se han insertado {len(alumnos_lista)} alumnos.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Hubo un error al insertar: {e}'))