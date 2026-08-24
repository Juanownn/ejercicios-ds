import models
from database.connection import engine
from database.base import Base
from sqlalchemy.orm import Session
from sqlalchemy import select

Base.metadata.create_all(engine)

with Session(engine) as session:
    """  
    departamento1 = models.Departamento(
        nombre="Ingenieria"
    )

    session.add(departamento1)
    session.commit()


    profesor1 = models.Profesor(
        nombre="Juano",
        email="juan@gmail.com",
        departamento_id=1
    )

    profesor2 = models.Profesor(
        nombre="Santiago",
        email="santiago@gmail.com",
        departamento_id=1
    )

    session.add_all([
        profesor1,
        profesor2
    ])

    session.commit() 
    
    curso1 = models.Curso(
        titulo="Algebra",
        creditos=100,
        profesor_id=1
    )

    curso2 = models.Curso(
            titulo="Desarrollo Web",
            creditos=100,
            profesor_id=1
    )

    curso3 = models.Curso(
            titulo="Sistemas Operativos",
            creditos=100,
            profesor_id=2
    )
    session.add_all([
        curso1,
        curso2,
        curso3
    ])

    session.commit()
    

    clase1 = models.Clase(
            tema="Matrices",
            duracion_minutos=50,
            curso_id=1
    )
    clase2 = models.Clase(
            tema="Determinante",
            duracion_minutos=60,
            curso_id=1
    )
    clase3 = models.Clase(
            tema="Python",
            duracion_minutos=120,
            curso_id=2
    )

    session.add_all([
        clase1,
        clase2,
        clase3
    ])

    session.commit()
    
    estudiante1 = models.Estudiante(
        nombre="Pepito",
        legajo=32
    )
    estudiante2 = models.Estudiante(
        nombre="Pablito",
        legajo=123
    )
    estudiante3 = models.Estudiante(
        nombre="Lucio",
        legajo=34
    )

    session.add_all([
        estudiante1,
        estudiante2,
        estudiante3
    ])
    session.commit()

    inscripcion1 = models.Inscripcion(
        estudiante_id=estudiante1.id,
        curso_id=curso1.id,
        calificacion_final=9
    )

    inscripcion2 = models.Inscripcion(
            estudiante_id=estudiante1.id,
            curso_id=curso2.id,
            calificacion_final=8
    )
     
    inscripcion3 = models.Inscripcion(
                estudiante_id=estudiante1.id,
                curso_id=curso3.id,
                calificacion_final=9
    )

    session.add_all([
        inscripcion1,
        inscripcion2,
        inscripcion3
    ])
    session.commit()
    """

    est1 = session.scalars(
        select(models.Estudiante)
    ).first()
    acum = 0
    for inscripcion in est1.inscripciones:
        acum+=inscripcion.calificacion_final
    prom=acum/len(est1.inscripciones)
    print(f"El promedio de {est1.nombre} es: {prom:.2f}")
    """ 
    departamentos = session.scalars(
        select(models.Departamento)
    ).all()

    for departamento in departamentos:
        print(f"Departamento: {departamento.nombre}")

        for profesor in departamento.profesores:
            print(f"Profesor: {profesor.nombre} | ID: {profesor.id}")
            print("Cursos dictados: ")
            for curso in profesor.cursos:
                print(curso.titulo)
                if len(curso.clases) > 0:
                    print("Clases vistas:")
                    for clase in curso.clases:
                        print(f"Tema: {clase.tema} que duro: {clase.duracion_minutos} min")
     """