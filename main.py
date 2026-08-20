from database.connection import engine
from database.base import Base
from models.profesor import Profesor
from sqlalchemy.orm import Session
from sqlalchemy import select

Base.metadata.create_all(engine)

with Session(engine) as session:
    """    
    profesor1 = Profesor(
        nombre="Juano",
        email="juan@gmail.com"
    )

    profesor2 = Profesor(
        nombre="Santiago",
        email="santiago@gmail.com"
    )

    session.add(profesor1)
    session.add(profesor2)

    session.commit()
    """
    stmt = select(Profesor)
    profesor1 = session.scalars(stmt).first()
    print(profesor1.id)
    print(profesor1.nombre)
    print(profesor1.email)