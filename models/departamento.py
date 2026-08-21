""" 1. Crear un nuevo modelo Departamento (id, nombre).
2. Modificar el modelo Profesor para agregarle una clave
foránea departamento_id.
3. Utilizar relationship en el modelo Departamento para
acceder a la lista de sus profesores.
 """

from database.base import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Departamento(Base):
    __tablename__ = "departamentos"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))

    #Relacion ORM para navegacion con Profesores
    profesores: Mapped[list["Profesor"]] = relationship(back_populates="departamento")