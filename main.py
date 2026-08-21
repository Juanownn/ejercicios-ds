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
    departamentos = session.scalars(
        select(models.Departamento)
    ).all()

    for departamento in departamentos:
        print(f"Departamento: {departamento.nombre}")

        for profesor in departamento.profesores:
            print(f"Profesor: {profesor.nombre} | ID: {profesor.id}")
    