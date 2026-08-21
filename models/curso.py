""" Crear el modelo Curso (id, titulo, creditos).
Un profesor puede dictar muchos cursos, pero un curso es
dictado por un único profesor.
Añadir la clave foránea profesor_id en Curso y la relación
correspondiente en ambos modelos (Profesor y Curso). """

from database.base import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Curso(Base):
    __tablename__ = "cursos"
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))
    creditos: Mapped[int]

    #clave foranea para profesor
    profesor_id: Mapped[int] = mapped_column(ForeignKey("profesores.id"))

    #Relacion con Profesor
    profesor: Mapped["Profesor"] = relationship(back_populates="cursos")