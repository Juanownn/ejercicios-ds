from database.base import Base
from sqlalchemy import Table, Column, ForeignKey, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

""" Implementacion de tabla inscripcion (Solo foreign key)
inscripcion = Table(
    "inscripcion",
    Base.metadata,

    Column(
        "estudiante_id",
        ForeignKey("estudiantes.id"),
        primary_key=True
    ),

    Column(
        "curso_id",
        ForeignKey("cursos.id"),
        primary_key=True
    )
)
"""

class Inscripcion(Base):
    __tablename__ = "inscripciones"
    estudiante_id: Mapped[int] = mapped_column(ForeignKey("estudiantes.id"), primary_key=True)
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"), primary_key=True)
    fecha_inscripcion: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    calificacion_final: Mapped[int]

    #Relaciones con Estudiante y con Curso
    estudiante: Mapped["Estudiante"] = relationship(back_populates="inscripciones")
    curso: Mapped["Curso"] = relationship(back_populates="inscripciones")