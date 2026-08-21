from database.base import Base
from pydantic import EmailStr
from datetime import datetime
from sqlalchemy import DateTime, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Profesor(Base):
    __tablename__ = "profesores"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))
    fecha_ingreso: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)

    #Clave foranea fisica de la DB
    departamento_id: Mapped[int] = mapped_column(ForeignKey("departamentos.id"))

    #Relacion ORM para navegacion con Departamento
    departamento: Mapped["Departamento"] = relationship(back_populates="profesores")

    #Relacion con Cursos
    cursos: Mapped[list["Curso"]] = relationship(back_populates="profesor")