from database.base import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
#from models.inscripcion import inscripcion

class Curso(Base):
    __tablename__ = "cursos"
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))
    creditos: Mapped[int]

    #clave foranea para profesor
    profesor_id: Mapped[int] = mapped_column(ForeignKey("profesores.id"))

    #Relacion con Profesor
    profesor: Mapped["Profesor"] = relationship(back_populates="cursos")

    #Relacion con Clase
    clases: Mapped[list["Clase"]] = relationship(back_populates="curso")

    """ Tabla inscripcion con foraneas unicamente
    relacion muchos a muchos a alumnos con tabla inscripcion intermedia
    estudiantes: Mapped[list["Estudiante"]] = relationship(
        secondary=inscripcion,
        back_populates="cursos"
    ) 
    """

    #Clase Inscripcion con informacion extra 
    #(Relacion con estudiante)
    inscripciones: Mapped[list["Inscripcion"]] = relationship(back_populates="curso")