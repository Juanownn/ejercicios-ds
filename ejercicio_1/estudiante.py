from pydantic import BaseModel, Field, EmailStr

class Estudiante(BaseModel):
    legajo: int = Field(ge=0, description="Numero mayor a 0")
    nomCompleto: str = Field(min_length=5)
    email: EmailStr
    promedio: float = Field(ge=0.0, le=10.0, default=0.0)

