from pydantic import BaseModel, Field, AnyUrl
from typing import Optional, Union

class PerfilUsuario(BaseModel):
    username: str = Field(pattern=r"^[a-z0-9_]{3,20}$")
    biografia: Optional[str] = Field(default=None, max_length=200)
    redes_sociales: Optional[list[Union[str, AnyUrl]]] = None

    