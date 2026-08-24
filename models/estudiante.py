from database.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
#from models.inscripcion import inscripcion

class Estudiante(Base):
    __tablename__ = "estudiantes"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    legajo: Mapped[int]

    """ Tabla inscripcion con foraneas unicamente
    #Relacion muchos a muchos a cursos con tabla inscripcion intermedia
    cursos: Mapped[list["Curso"]] = relationship(
        secondary=inscripcion,
        back_populates="estudiantes"
    )
    """

    #Clase Inscripcion con informacion extra 
    #(Relacion con curso)
    inscripciones: Mapped[list["Inscripcion"]] = relationship(back_populates="estudiante")