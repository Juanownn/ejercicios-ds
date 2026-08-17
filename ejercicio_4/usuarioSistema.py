from pydantic import BaseModel, Field, EmailStr

class UsuarioSistema(BaseModel):
    email: EmailStr
    nivel_acceso: int = Field(ge=1, le=5, description="Nivel de Acceso")
