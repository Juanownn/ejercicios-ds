from database.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

class Clase(Base):
    __tablename__ = "clases"
    id: Mapped[int] = mapped_column(primary_key=True)
    tema: Mapped[str] = mapped_column(String(100))
    duracion_minutos: Mapped[int]

    #clave foranea para profesor
    curso_id: Mapped[int] = mapped_column(ForeignKey("cursos.id"))

    #relacion con Curso
    curso: Mapped["Curso"] = relationship(back_populates="clases")