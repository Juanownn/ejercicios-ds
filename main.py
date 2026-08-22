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
    """
    """ 
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
                print("Clases vistas:")
                for clase in curso.clases:
                    print(f"Tema: {clase.tema} que duro: {clase.duracion_minutos} min")
    